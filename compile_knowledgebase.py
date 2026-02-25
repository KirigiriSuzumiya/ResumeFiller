from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tools import vector_store
from config.llm import qwen_embeddings_batch_size

file_path = "knowledge/resume.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=100, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

for batch in [all_splits[i:i+qwen_embeddings_batch_size] for i in range(0, len(all_splits), qwen_embeddings_batch_size)]:
    vector_store.add_documents(batch)