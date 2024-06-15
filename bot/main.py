# bot/main.py

import time
import schedule
from bot.config import EXCEL_FILE_PATH, CHECK_INTERVAL
from bot.excel_monitor import ExcelMonitor
from bot.telegram_notifier import send_message
from bot.utils import setup_logging, log_info, log_error

def check_excel_file():
    log_info("Checking Excel file for changes.")
    try:
        added_data, modified_data = excel_monitor.check_for_changes()
        if added_data is not None and not added_data.empty:
            log_info(f"New data added: {added_data}")
            send_message(f"New data added: {added_data}")
        if modified_data is not None and not modified_data.empty:
            log_info(f"Existing data modified: {modified_data}")
            send_message(f"Existing data modified: {modified_data}")
    except Exception as e:
        log_error(f"Error checking Excel file: {e}")

# Setup logging
setup_logging()
log_info("Logging is set up.")

# Initialize the Excel monitor
log_info(f"Initializing Excel monitor for file: {EXCEL_FILE_PATH}")
excel_monitor = ExcelMonitor(EXCEL_FILE_PATH)

# Schedule the task
log_info(f"Scheduling Excel file checks every {CHECK_INTERVAL} minutes.")
schedule.every(CHECK_INTERVAL).minutes.do(check_excel_file)

log_info("Scheduler setup complete. Entering main loop...")

while True:
    schedule.run_pending()
    log_info("Scheduled tasks checked.")
    time.sleep(1)
