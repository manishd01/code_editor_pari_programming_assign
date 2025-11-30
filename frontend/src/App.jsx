// App.js
import React, { useEffect, useState } from "react";
import Editor from "./Editor";
import { createRoom } from "./api";

import { BACKEND } from "./api";

function App() {
  const [roomId, setRoomId] = useState(null);
  const [language, setLanguage] = useState("python");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const match = window.location.pathname.match(/\/room\/(.+)/);
    if (match) {
      const id = match[1];
      setRoomId(id);
      setLoading(true);

      // Fetch existing room info
      fetch(`${BACKEND}/rooms/${id}`)
        .then((res) => res.json())
        .then((data) => {
          setLanguage(data.language || "python");
        })
        .finally(() => setLoading(false));
    }
  }, []);
  async function startNew() {
    setLoading(true);
    try {
      const data = await createRoom(language);
      console.log("Created room:", data);
      const id = data.roomId;
      window.history.pushState({}, "", `/room/${id}`);
      setRoomId(id);
    } catch (err) {
      console.error("Failed to create room:", err);
      alert("Failed to create room. Check backend logs.");
    } finally {
      setLoading(false);
    }
  }

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ padding: 16 }}>
      <h2>PairCodr Minimal</h2>

      {!roomId ? (
        <>
          <button onClick={startNew}>Create new room</button>

          <div style={{ marginTop: 12 }}>
            Or join via URL <code>/room/&lt;roomId&gt;</code>
          </div>

          {/* LANGUAGE DROPDOWN */}
          <div style={{ marginTop: 20 }}>
            <label>Select language: </label>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
            >
              <option value="python">Python</option>
              <option value="javascript">JavaScript</option>
              <option value="html">HTML</option>
              <option value="cpp">C++</option>
            </select>
          </div>
        </>
      ) : (
        <Editor roomId={roomId} language={language} />
      )}
    </div>
  );
}

export default App;

// App.js
// import React, { useEffect, useState } from "react";
// import Editor from "./Editor";
// import { createRoom } from "./api";

// function App() {
//   const [roomId, setRoomId] = useState(null);
//   const [language, setLanguage] = useState("python");

//   // If URL contains /room/<id>, extract it
//   useEffect(() => {
//     const match = window.location.pathname.match(/\/room\/(.+)/);
//     if (match) {
//       setRoomId(match[1]);
//     }
//   }, []);

//   async function startNew() {
//     const data = await createRoom(language); // pass selected language
//     const id = data.roomId;
//     window.history.pushState({}, "", `/room/${id}`);
//     setRoomId(id);
//   }

//   return (
//     <div style={{ padding: 16 }}>
//       <h2>PairCodr Minimal</h2>

//       {!roomId ? (
//         <>
//           <button onClick={startNew}>Create new room</button>

//           <div style={{ marginTop: 12 }}>
//             Or join via URL <code>/room/&lt;roomId&gt;</code>
//           </div>

//           {/* LANGUAGE DROPDOWN */}
//           <div style={{ marginTop: 20 }}>
//             <label>Select language: </label>
//             <select
//               value={language}
//               onChange={(e) => setLanguage(e.target.value)}
//             >
//               <option value="python">Python</option>
//               <option value="javascript">JavaScript</option>
//               <option value="html">HTML</option>
//               <option value="cpp">C++</option>
//             </select>
//           </div>
//         </>
//       ) : (
//         <Editor roomId={roomId} language={language} />
//       )}
//     </div>
//   );
// }

// export default App;
