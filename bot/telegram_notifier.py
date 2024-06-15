import logging
from telegram import Bot
from telegram.error import TelegramError
from bot.config import TELEGRAM_TOKEN, CHAT_ID
from bot.config import LOG_FILE_PATH

# Initialize the Telegram bot
bot = Bot(token=TELEGRAM_TOKEN)

def send_message(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        logging.info(f"Message sent successfully: {message}")
    except TelegramError as e:
        logging.error(f"Failed to send message: {e}")

def notify_changes(added, modified):
    if added is not None and not added.empty:
        send_message(f"New data added:\n{added}")
    if modified is not None and not modified.empty:
        send_message(f"Data modified:\n{modified}")

# Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
