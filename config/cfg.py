from dotenv import load_dotenv
import os

# config
load_dotenv("cfg.env")
chrome_debug_server_url = os.getenv("CHROME_DEBUG_SERVER_URL")
