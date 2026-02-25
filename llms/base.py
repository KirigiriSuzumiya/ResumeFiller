from langchain_openai import ChatOpenAI
from config.llm import openai_api_base, openai_api_key, request_timeout_sec
from config.llm import qwen_chat_model, qwen_chat_model_max_token
from config.llm import qwen_code_model, qwen_code_model_max_token

base_chat_model = ChatOpenAI(
    model=qwen_chat_model,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    max_tokens=qwen_chat_model_max_token,
    request_timeout=request_timeout_sec,
    model_kwargs={ "tool_choice": "auto"},
    extra_body={"enable_thinking": False}
)

base_code_model = ChatOpenAI(
    model=qwen_code_model,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    max_tokens=qwen_code_model_max_token,
    request_timeout=request_timeout_sec,
)