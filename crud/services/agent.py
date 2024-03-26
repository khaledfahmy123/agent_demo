from uuid import UUID
from typing import AsyncGenerator, List, Dict, Any

from langchain_core.outputs import LLMResult
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.callbacks import BaseCallbackHandler
from langchain import hub

from models.schemas.chat import ChatRequest

class AgentObserver(BaseCallbackHandler):
    async def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"My custom handler, token: {token}")

    async def on_llm_end(self, response: LLMResult, *, run_id: UUID, parent_run_id: UUID | None = None, **kwargs: Any) -> Any:
        l = {**kwargs}
        print(l, response)



class CBio_Portal_Agent():
    
    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    sources = []
    
    def __init__(self, vectorstore) -> None:
        self.retriever = vectorstore.as_retriever()

    async def generate_response(self, message: str) -> AsyncGenerator[str, None]:
        
        rag_chain_from_docs = (RunnablePassthrough.assign(context=(lambda x: self.format_docs(x["context"]))) | self.prompt | self.llm | StrOutputParser())
        
        rag_chain_with_source = RunnableParallel({"context": self.retriever, "question": RunnablePassthrough()}).assign(answer=rag_chain_from_docs)
        
        async for chunk in rag_chain_with_source.astream(message):
            if "answer" in chunk:
                yield chunk["answer"]

    async def start_chat(self, data: Dict[str, Any]):
        request = ChatRequest(**data)

        async for content in self.generate_response(message=request.message):
            yield content
    
    def format_docs(self, docs):
        print(docs)
        self.sources = ["https://github.com/cBioPortal/cbioportal/tree/master/docs" + doc.metadata["source"][26:] for doc in docs]
        return "\n\n".join(doc.page_content for doc in docs)