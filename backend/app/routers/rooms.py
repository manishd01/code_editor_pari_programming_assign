
# backend/app/routers/rooms.py
import uuid
from fastapi import APIRouter, HTTPException
from .. import db, models
from ..schemas import CreateRoomRequest, CreateRoomResponse
from ..schemas import AutocompleteRequest, AutocompleteResponse
from ..rules.lang_rules import python_rules, javascript_rules, html_rules, cpp_rules

router = APIRouter()

@router.post("/rooms", response_model=CreateRoomResponse)
def create_room(req: CreateRoomRequest):
    room_id = str(uuid.uuid4())[:8]
    session = db.SessionLocal()
    try:
        room = models.Room(id=room_id, code="", language=req.language)
        session.add(room)
        session.commit()
    finally:
        session.close()
    return {"roomId": room_id}

@router.get("/rooms/{room_id}")
def get_room(room_id: str):
    session = db.SessionLocal()
    try:
        room = session.query(models.Room).filter(models.Room.id == room_id).first()
        if not room:
            raise HTTPException(status_code=404, detail="Room not found")
        return {"roomId": room.id, "code": room.code, "language": room.language}
    finally:
        session.close()
 


 
#  //1:: manual implementation of autocomplete rules
@router.post("/autocomplete", response_model=AutocompleteResponse)
def autocomplete(req: AutocompleteRequest):
    """
    Mocked autocomplete: looks at last 20 chars before cursor and
    returns a suggestion based on language rules.
    """
    text = req.code
    pos = req.cursorPosition
    prefix = text[max(0, pos-20):pos].strip()

    lang = req.language.lower()
    suggestion = ""
    if lang == "python":
        suggestion = python_rules(prefix)
    elif lang == "javascript":
        suggestion = javascript_rules(prefix)
    elif lang == "html":
        suggestion = html_rules(prefix)
    elif lang == "cpp":
        suggestion = cpp_rules(prefix)

    print(f"AUTOCOMPLETE ({lang}): {suggestion}")
    return {"suggestion": suggestion}



# # # backend/app/routers/rooms.py

# # router = APIRouter()
# import uuid
# import requests

# # # https://console.groq.com/keys
# # url = "https://api.groq.com/openai/v1/chat/completions"



import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    



# # 2: GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
# # this is using externam api: (not manual implementation)
# # @router.post("/autocomplete", response_model=AutocompleteResponse)
# # def autocomplete_route(req: AutocompleteRequest):
# #     url = "https://api.groq.com/openai/v1/chat/completions"
# #     headers = {
# #         "Authorization": "Bearer  {GROQ_API_KEY}",
# #         "Content-Type": "application/json"
# #     }

# #     data = {
# #         "model": "llama-3.1-8b-instant",
# #         "messages": [
# #             {"role": "system", "content": "You are an AI code autocompleter."},
# #             {"role": "user", "content": req.code}
# #         ],
# #         "max_tokens": 40,
# #         "temperature": 0.2
# #     }

# #     try:
# #         r = requests.post(url, json=data, headers=headers, timeout=10)
# #         print("STATUS:", r.status_code)
# #         print("TEXT:", r.text)

# #         r.raise_for_status()
# #         suggestion = r.json()["choices"][0]["message"]["content"]

# #     except Exception as e:
# #         print(" AUTOCOMPLETE ERROR:", e)
# #         suggestion = ""

# #     return {"suggestion": suggestion}




