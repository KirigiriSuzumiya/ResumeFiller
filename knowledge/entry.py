from models import FormField
from tools import vector_store
from langchain_core.documents import Document

def information_entry(field_name: str, field_value: str):
    vector_store.add_documents(
        [
            Document(
                page_content=f"{field_name}: {field_value}",
                metadata={"source":"manual_input"}
            )
        ]
    )