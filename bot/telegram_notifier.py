# bot/telegram_notifier.py

from telegram import Bot
from bot.config import TELEGRAM_TOKEN, CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def notify_changes(added, modified):
    if added is not None and not added.empty:
        send_message(f"New data added:\n{added}")
    if modified is not None and not modified.empty:
        send_message(f"Data modified:\n{modified}")
