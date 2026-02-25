from langchain_openai import ChatOpenAI
from config.model import openai_api_base, openai_api_key, request_timeout_sec
from config.model import qwen_chat_model, qwen_chat_model_max_token
from config.model import qwen_code_model, qwen_code_model_max_token

base_chat_model = ChatOpenAI(
    model=qwen_chat_model,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    max_tokens=qwen_chat_model_max_token,
    request_timeout=request_timeout_sec,
)

base_code_model = ChatOpenAI(
    model=qwen_code_model,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    max_tokens=qwen_code_model_max_token,
    request_timeout=request_timeout_sec,
)