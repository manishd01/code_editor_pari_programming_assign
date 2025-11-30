// frontend/src/api.js

export const BACKEND =
  process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

export async function createRoom(language = "python") {
  const res = await fetch(`${BACKEND}/rooms`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ language }),
  });
  // console.error(await res.text());

  if (!res.ok) {
    console.error(await res.text());
    throw new Error("Failed to create room"); // this is why your app gets stuck
  }

  return res.json();
}

export async function autocomplete(payload) {
  // payload is expected to have: { code, cursorPosition, language }
  const res = await fetch(`${BACKEND}/autocomplete`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}
