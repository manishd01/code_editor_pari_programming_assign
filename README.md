# README

## 1. Project Summary

This project is a simplified **real-time pair-programming prototype**
built using:

-   **Backend:** Python, FastAPI, WebSockets\
-   **Frontend (optional):** React + TypeScript

### Basic Features

1.  Create or join rooms for collaborative coding\
2.  Real-time code synchronization using WebSockets\
3.  Mock AI autocomplete via `POST /autocomplete`

------------------------------------------------------------------------

## 2. Directory Structure

    backend/
     ├── app/
     │    ├── main.py
     │    ├── routers/
     │    ├── services/
     │    ├── schemas.py
     │    ├── ws_manager.py
     ├── requirements.txt

    frontend/ (optional)
     ├── src/
     │    ├── App.tsx
     │    ├── Editor.tsx
     │    ├── store/
     │    ├── api.ts

------------------------------------------------------------------------

## 3. Setup Instructions

### 3.1 Backend Setup

1.  cd backend
2.  python -m venv venv
3.  Activate environment:
    -   Linux/Mac: source venv/bin/activate\
    -   Windows: venv`\Scripts`{=tex}`\activate`{=tex}
4.  pip install -r requirements.txt
5.  uvicorn app.main:app --reload

------------------------------------------------------------------------

### 3.2 Frontend Setup (Optional)

1.  cd frontend
2.  npm install
3.  npm start

------------------------------------------------------------------------

## 4. Access URLs

-   Backend: http://localhost:8000\
-   Frontend: http://localhost:3000
