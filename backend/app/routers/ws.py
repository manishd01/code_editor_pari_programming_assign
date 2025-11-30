# backend/app/routers/ws.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .. import db, models
from ..ws_manager import manager, save_room_state_to_db

router = APIRouter()

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(room_id, websocket)

    # send initial room state from DB
    session = db.SessionLocal()
    try:
        room = session.query(models.Room).filter(models.Room.id == room_id).first()
        if not room:
            room = models.Room(id=room_id, code="", language="python")
            session.add(room)
            session.commit()
        await websocket.send_json({
            "type": "room_info",
            "code": room.code,
            "language": room.language
        })
    finally:
        session.close()

    try:
        while True:
            data = await websocket.receive_json()
            if data["type"] == "code_update":
                # Save to DB
                save_room_state_to_db(room_id, data["code"])
                # Broadcast to other clients
                await manager.broadcast(room_id, {"type": "code_update", "code": data["code"]}, sender=websocket)

            elif data["type"] == "language_change":
                save_room_state_to_db(room_id, data.get("code", ""), data["language"])
                await manager.broadcast(room_id, {"type": "language_update", "language": data["language"]}, sender=websocket)

    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
    except Exception:
        manager.disconnect(room_id, websocket)
