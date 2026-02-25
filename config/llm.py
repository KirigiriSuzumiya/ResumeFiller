from dotenv import load_dotenv
import os

# model config
load_dotenv("cfg.env")
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")
request_timeout_sec = int(os.getenv("REQUEST_TIMEOUT_SEC"))


qwen_chat_model = os.getenv("QWEN_CHAT_MODEL")
qwen_chat_model_max_token = int(os.getenv("QWEN_CHAT_MODEL_MAX_TOKENS"))

qwen_code_model = os.getenv("QWEN_CODE_MODEL")
qwen_code_model_max_token = int(os.getenv("QWEN_CODE_MODEL_MAX_TOKENS"))

qwen_embeddings_model = os.getenv("QWEN_EMBEDDINGS_MODEL")
qwen_embeddings_batch_size = int(os.getenv("QWEN_EMBEDDINGS_BATCH_SIZE"))
