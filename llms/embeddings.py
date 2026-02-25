from langchain_openai import OpenAIEmbeddings
from config.llm import openai_api_base, openai_api_key
from config.llm import qwen_embeddings_model

embeddings_model = OpenAIEmbeddings(
    model=qwen_embeddings_model,
    base_url=openai_api_base,
    api_key=openai_api_key,
    check_embedding_ctx_length=False,
)