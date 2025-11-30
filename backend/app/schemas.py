from pydantic import BaseModel
from typing import Optional

class CreateRoomResponse(BaseModel):
    roomId: str

class CreateRoomRequest(BaseModel):
    language: str 

class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: str

class AutocompleteResponse(BaseModel):
    suggestion: str

class RoomState(BaseModel):
    roomId: str
    code: str
    language: Optional[str] = "python"
