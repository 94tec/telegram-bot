# Telegram Bot Service

This project is a Telegram bot service that monitors changes in an Excel file and sends notifications via Telegram when new data is added or existing data is modified.

## Project Structure

telegram bot service/
├── bot/
│ ├── init.py
│ ├── config.py
│ ├── main.py
│ ├── excel_monitor.py
│ ├── telegram_notifier.py
│ └── utils.py
├── data/
│ └── data.xlsx
├── logs/
│ └── bot.log
├── tests/
│ ├── init.py
│ ├── test_excel_monitor.py
│ ├── test_telegram_notifier.py
│ └── test_utils.py
├── venv/
│ └── ... (virtual environment files)
├── .gitignore
├── requirements.txt
└── README.md


## Requirements

- Python 3.7+
- pip (Python package installer)
- A Telegram bot token
- A chat ID to send messages to

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/94tec/telegram-bot.git
    cd telegram-bot
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the bot:**

    Edit the `bot/config.py` file to add your Telegram bot token, chat ID, Excel file path, and check interval.

    ```python
    # bot/config.py
    BOT_TOKEN = 'your-telegram-bot-token'
    CHAT_ID = 'your-chat-id'
    EXCEL_FILE_PATH = 'path/to/your/data.xlsx'
    CHECK_INTERVAL = 1  # Check interval in minutes
    LOG_FILE_PATH = 'C:/94tecprocs/telegram bot service/logs/bot.log'
    ```

5. **Ensure the data and logs directories exist:**

    Make sure `data/` contains your `data.xlsx` file and `logs/` directory exists.

    ```bash
    mkdir -p data logs
    touch logs/bot.log
    ```

## Running the Bot

1. **Activate the virtual environment (if not already activated):**

    ```bash
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Run the bot:**

    ```bash
    python -m bot.main
    ```

The bot will start and periodically check the Excel file for changes based on the configured interval. Log entries will be written to `logs/bot.log`.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover -s tests


Certainly! Here’s a template for a README file for your Telegram Bot project. This file provides an overview of the project, instructions on how to set it up, and how to run it. Save this content to a file named README.md in your project root directory.

markdown
Copy code
# Telegram Bot Service

This project is a Telegram bot service that monitors changes in an Excel file and sends notifications via Telegram when new data is added or existing data is modified.

## Project Structure

telegram_bot/
├── bot/
│ ├── init.py
│ ├── config.py
│ ├── main.py
│ ├── excel_monitor.py
│ ├── telegram_notifier.py
│ └── utils.py
├── data/
│ └── data.xlsx
├── logs/
│ └── bot.log
├── tests/
│ ├── init.py
│ ├── test_excel_monitor.py
│ ├── test_telegram_notifier.py
│ └── test_utils.py
├── venv/
│ └── ... (virtual environment files)
├── .gitignore
├── requirements.txt
└── README.md

r
Copy code

## Requirements

- Python 3.7+
- pip (Python package installer)
- A Telegram bot token
- A chat ID to send messages to

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/telegram_bot_service.git
    cd telegram_bot_service
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the bot:**

    Edit the `bot/config.py` file to add your Telegram bot token, chat ID, Excel file path, and check interval.

    ```python
    # bot/config.py
    BOT_TOKEN = 'your-telegram-bot-token'
    CHAT_ID = 'your-chat-id'
    EXCEL_FILE_PATH = 'path/to/your/data.xlsx'
    CHECK_INTERVAL = 1  # Check interval in minutes
    LOG_FILE_PATH = 'C:/94tecprocs/telegram bot service/logs/bot.log'
    ```

5. **Ensure the data and logs directories exist:**

    Make sure `data/` contains your `data.xlsx` file and `logs/` directory exists.

    ```bash
    mkdir -p data logs
    touch logs/bot.log
    ```

## Running the Bot

1. **Activate the virtual environment (if not already activated):**

    ```bash
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Run the bot:**

    ```bash
    python -m bot.main
    ```

The bot will start and periodically check the Excel file for changes based on the configured interval. Log entries will be written to `logs/bot.log`.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover -s tests

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
If you wish to contribute to this project, please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding standards and passes all tests.

## Contact
If you have any questions or issues, feel free to open an issue on the repository or contact me at fixtone94tec@gmail.com.


