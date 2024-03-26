import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_docs():
    doc_path = "resources/global_pdfs/cbioportal/docs"
    
    docs = DirectoryLoader(doc_path, glob="**/*.md")
    docs = docs.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    docs_splitted = text_splitter.split_documents(docs)
    
    return docs_splitted