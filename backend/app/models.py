# backend/app/models.py
from sqlalchemy import Column, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = "rooms"
    id = Column(String(64), primary_key=True, index=True)
    code = Column(Text, default="")              # store code
    language = Column(String(32), default="python")  # store selected language
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
