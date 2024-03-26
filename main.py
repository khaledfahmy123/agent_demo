import uvicorn
import contextlib
import os
import socketio
from dotenv import load_dotenv
from fastapi import FastAPI
from dependencies import get_vectorstore
from fastapi.middleware.cors import CORSMiddleware
from socket_manager import socket_app
import routers.agent_events # don't remove
from utils.init_chroma_helper import load_docs
import sys


load_dotenv()

__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.path.exists("db"):
        os.makedirs("db")

    vectorstore = get_vectorstore()
    
    is_collection_empty: bool = vectorstore._collection.count() == 0

    if is_collection_empty:
        docs = load_docs()
        vectorstore.add_documents(docs)

    if not os.path.exists("resources/message_store"):
        os.mkdir("resources/message_store")
    
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", socket_app)




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)