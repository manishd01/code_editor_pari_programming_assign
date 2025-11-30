import React, { useEffect, useState, useRef } from "react";

export default function Editor({ roomId, language, setLanguage }) {
  const socketRef = useRef(null);
  const [code, setCode] = useState("");
  const [suggestion, setSuggestion] = useState("");
  const textareaRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/ws/${roomId}`);
    socketRef.current = ws;

    ws.onopen = () => console.log("🔗 Connected to WS");
    ws.onerror = (e) => console.log("❌ WS error:", e);

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);

      if (msg.type === "room_info") {
        setCode(msg.code || "");
        if (setLanguage) setLanguage(msg.language);
      }

      if (msg.type === "code_update") setCode(msg.code);
      if (msg.type === "language_update" && setLanguage)
        setLanguage(msg.language);
    };

    return () => ws.close();
  }, [roomId, setLanguage]);

  function handleChange(e) {
    const updated = e.target.value;
    setCode(updated);

    // ✅ Only send if socket is open
    if (socketRef.current?.readyState === WebSocket.OPEN) {
      socketRef.current.send(
        JSON.stringify({ type: "code_update", code: updated })
      );
    }
  }

  async function triggerAutocomplete() {
    const cursorPos = textareaRef.current.selectionStart;

    const res = await fetch("http://localhost:8000/autocomplete", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, cursorPosition: cursorPos, language }),
    });

    const data = await res.json();
    setSuggestion(data.suggestion);
  }

  // inside Editor component
  async function applySuggestion() {
    const textarea = textareaRef.current;
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;

    const newCode = code.substring(0, start) + suggestion + code.substring(end);
    setCode(newCode);
    setSuggestion("");

    // send update to WebSocket if open
    if (socketRef.current?.readyState === WebSocket.OPEN) {
      socketRef.current.send(
        JSON.stringify({ type: "code_update", code: newCode })
      );
    }
  }

  return (
    <div style={{ padding: 12 }}>
      <h3>Room: {roomId}</h3>
      <p>
        <b>Language:</b> {language}
      </p>
      <textarea
        ref={textareaRef}
        value={code}
        onChange={handleChange}
        onKeyUp={triggerAutocomplete}
        rows={20}
        cols={80}
        style={{ fontFamily: "monospace", padding: 10 }}
      />

      {suggestion && (
        <div
          style={{
            marginTop: 10,
            padding: 8,
            background: "#222",
            color: "lightgreen",
            borderRadius: 4,
          }}
        >
          <p>Suggestion: {suggestion}</p>
          <button onClick={applySuggestion}>Apply</button>
        </div>
      )}
    </div>
  );
}
