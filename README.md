## Project Summary

This project is a simplified real-time pair-programming prototype built using:

Backend: Python, FastAPI, WebSockets
Frontend: React + TypeScript (optional)

Basic Features:

- Create or join rooms for collaborative coding
- Real-time code sync using WebSockets
- Mock AI autocomplete via POST /autocomplete

## Directory Structure

backend/
app/
main.py
routers/
services/
schemas.py
ws_manager.py
requirements.txt

frontend/ (optional)
src/
App.jsx
Editor.jsx
api.js
index.js

## Setup Instructions

1. Backend Setup:
   cd backend
   python -m venv venv
   source venv/bin/activate (Windows: venv\Scripts\activate)
   pip install -r requirements.txt
   uvicorn app.main:app --reload

2. Frontend Setup (optional):
   cd frontend
   npm install
   npm start
3: setup postgre database credentials- (create .envfile in both folders)

## Access

Backend runs at: http://localhost:8000
Frontend runs at: http://localhost:3000
