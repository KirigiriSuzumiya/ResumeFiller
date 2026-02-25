from langchain_chroma import Chroma
from llms import embeddings_model
from config.cfg import chroma_persist_directory

vector_store = Chroma(
    embedding_function=embeddings_model,
    persist_directory=chroma_persist_directory,
)