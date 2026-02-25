from langchain.tools import tool
from .vector_store import vector_store

@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to fill the form."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs