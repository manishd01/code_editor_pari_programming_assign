// frontend/src/index.jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Set backend WebSocket URL globally
window.__BACKEND_WS__ = process.env.REACT_APP_WS_URL || "ws://localhost:8000";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
