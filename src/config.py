import os

from dotenv import dotenv_values, load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", None)
log_format = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

