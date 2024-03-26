import socketio
# from main import app
sio=socketio.AsyncServer(cors_allowed_origins=[],async_mode='asgi')
socket_app = socketio.ASGIApp(sio)


@sio.on("connect")
async def connect(sid, env):
    print("New Client Connected to This id :"+" "+str(sid))


@sio.on("disconnect")
async def disconnect(sid):
    print("Client Disconnected: "+" "+str(sid))