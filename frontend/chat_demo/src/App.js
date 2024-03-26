import Chat from './Components/Chat';
import { socket } from './socket';
import { useEffect, useState } from 'react';

function App() {
  const [connected, setConnected] = useState(false)
  useEffect(() => {
    
    const onConnect = () => {
      console.log("Socket Connected");
      setConnected(true)
      
    };

    const onDisConnect = () => {
      console.log("Socket Disconnected");
      setConnected(false)
    };

    socket.on("connect", onConnect);

    return () => {
      socket.off("connect", onDisConnect);
    };
  }, []);
  return (
    <Chat connected={connected}/>
  );
}

export default App;
