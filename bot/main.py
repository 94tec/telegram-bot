# bot/main.py
import time
import schedule
from bot.config import EXCEL_FILE_PATH, CHECK_INTERVAL
from bot.excel_monitor import ExcelMonitor
from bot.telegram_notifier import notify_changes
from bot.utils import setup_logging, log_info


def job():
    log_info("Checking for changes in the Excel file...")
    added, modified = excel_monitor.check_for_changes()
    notify_changes(added, modified)
    log_info("Finished checking for changes.")

if __name__ == "__main__":
    setup_logging()
    # Your main script logic goes here
    log_info("Starting the bot...")
    excel_monitor = ExcelMonitor(EXCEL_FILE_PATH)
    schedule.every(CHECK_INTERVAL).seconds.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

