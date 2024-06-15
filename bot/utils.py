# bot/utils.py

import logging
import os
from bot.config import LOG_FILE_PATH

def setup_logging():
    log_dir = os.path.dirname(LOG_FILE_PATH)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
