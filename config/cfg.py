from dotenv import load_dotenv
import os

# config
load_dotenv("cfg.env")

chroma_persist_directory = os.getenv("CHROMA_PERSIST_DIRECTORY")

