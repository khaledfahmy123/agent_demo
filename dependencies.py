from contextlib import asynccontextmanager
from langchain_community.vectorstores import Chroma
from functools import lru_cache
from models.schemas.chat import Settings
from langchain_openai import OpenAIEmbeddings        

@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore


@lru_cache()
def get_vectorstore() -> Chroma:
    settings = get_settings()

    embeddings = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)  # type: ignore

    vectorstore = Chroma(
        collection_name="chroma",
        embedding_function=embeddings,
        persist_directory="db/chroma",
    )

    return vectorstore


