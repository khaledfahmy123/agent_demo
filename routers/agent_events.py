from socket_manager import sio
from dependencies import get_vectorstore
from crud.services.agent import CBio_Portal_Agent

@sio.event
async def chat(sid, data):
    vectorstore = get_vectorstore()
    agent = CBio_Portal_Agent(vectorstore)
    async for content in agent.start_chat(data):
        await sio.emit('response', {'data': content, "done": False}, to=sid)
        
    await sio.emit('response', {'data': "", 'done': True, "sources": agent.sources}, to=sid)
