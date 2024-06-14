import os
import logging
from bot.config import LOG_FILE_PATH

# Create logs directory if it doesn't exist
logs_dir = os.path.dirname(LOG_FILE_PATH)
os.makedirs(logs_dir, exist_ok=True)

def setup_logging():
    log_directory = os.path.dirname(LOG_FILE_PATH)
    os.makedirs(log_directory, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
