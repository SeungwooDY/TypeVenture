"use client";

import Image from "next/image";
import { useState } from "react";

export default function Home() {

  const [story, setStory] = useState(
    "You wake up in an abandoned castle. Where do you want to go?"
  );

  const [command, setCommand] = useState("");

  function handleCommand() {
    // Send command to backend
    if (!command.trim()) return;

    let response = "";
    switch(command.toLowerCase()) {
      case "north":
        response = "You walk north and find a dark hallway.";
        break;

      default:
        response = "You can't go that way.";
    }

    setStory((prev) => + "\n\n> " + command + "\n" + response);
    setCommand("");
  }
  
  return (
    <main className="flex">
      <h1>Welcome to TextVenture!</h1>
      <textarea
        readOnly
        value={story}
        rows={10}
        style={{ width: "100%", marginBottom: "10px" }}
      />
      <input
        type="text"
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Enter command..."
        style={{ width: "100%", marginBottom: "10px" }}
      />
      <button onClick={handleCommand} style={{ width: "100%" }}>
        Submit
      </button>
    </main>
  );
}
