import { useState } from "react";
import { socket } from "../socket";


export const useChat = (initialValues) => {

  const [messages, setMessages] = useState([
    { direction: "incoming", message: "Hello! How can i help you?"},
  ]);

  const [wait, setWait] = useState(false);

  const [sources, setSources] = useState([]);



  const logHandler = (data) => {
    if (!data["done"]) {
      setMessages((prev) => {
        if (prev[prev.length - 1].direction === "incoming") {
          let msg = prev.pop();
          return [
            ...prev,
            {
              direction: "incoming",
              message: msg.message + data["data"],
            },
          ];
        }
        return [
          ...prev,
          {
            direction: "incoming",
            message: data["data"],
          },
        ];
      });
      return;
    }

    setSources(data["sources"])

    setWait(false);
    socket.off("response");
  };



  // Handle changes to form inputs
  const sendMessage = (msg) => {
    setMessages((prev) => [...prev, { direction: "outgoing", message: msg }]);
    try {
      socket.on("response", logHandler);
      socket.emit("chat", {
        session_id: "session_1",
        message: msg
      });
    } catch (error) {
      console.log("Error fetching data:", error);

      setWait(false);

      setMessages((prev) => [
        ...prev,
        {
          direction: "incoming",
          message: error.message,
        },
      ]);
    }
  };

  return [messages, sendMessage, wait, sources];
};
