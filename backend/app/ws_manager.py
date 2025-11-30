# backend/app/ws_manager.py
from typing import Dict, List
from fastapi import WebSocket
from sqlalchemy.orm import Session
from . import db, models

class ConnectionManager:
    def __init__(self):
        self.active: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active.setdefault(room_id, []).append(websocket)
        print(f"✅ Client connected to room {room_id}, total: {len(self.active[room_id])}")

    def disconnect(self, room_id: str, websocket: WebSocket):
        conns = self.active.get(room_id)
        if conns and websocket in conns:
            conns.remove(websocket)
            if not conns:
                self.active.pop(room_id)
        print(f"❌ Client disconnected from room {room_id}")

    async def broadcast(self, room_id: str, message: dict, sender: WebSocket = None):
        conns = self.active.get(room_id, [])
        for ws in conns.copy():
            if ws != sender:
                try:
                    await ws.send_json(message)
                except Exception:
                    await ws.close()
                    self.disconnect(room_id, ws)
                    print(f"⚠️ Failed sending message, removed client from room {room_id}")

manager = ConnectionManager()

def save_room_state_to_db(room_id: str, code: str, language: str = None):
    session: Session = db.SessionLocal()
    try:
        room = session.query(models.Room).filter(models.Room.id == room_id).first()
        if room:
            room.code = code
            if language:
                room.language = language
        else:
            room = models.Room(id=room_id, code=code, language=language)
            session.add(room)
        session.commit()
    finally:
        session.close()
