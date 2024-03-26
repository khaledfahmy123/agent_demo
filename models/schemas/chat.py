from pydantic import BaseModel
from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    openai_api_key: str
    langchain_tracing_v2: bool
    langchain_endpoint: str
    langchain_api_key: str
    langchain_project: str

    class Config:  # type: ignore
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


class ChatRequest(BaseModel):
    session_id: str
    message: str
