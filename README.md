# Telegram Obscene Word Tracking Bot

This bot tracks the usage of obscene words in a Telegram chat. It provides statistics on the number of obscene words used by each participant and the total number of obscene words used per day.

## Features

- Track obscene words in the chat.
- Provide statistics for each participant.
- Provide daily statistics for the chat.

## Commands

- `/start` - Start the bot and receive a welcome message.
- `/help` - Display help information.
- `/userstats` - Show the statistics of obscene words used by each participant.
- `/dailystats` - Show the daily statistics of obscene words used in the chat.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/telegram-obscene-word-tracking-bot.git
    cd telegram-obscene-word-tracking-bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `config.py` file and add your bot token:

    ```python
    # config.py
    TOKEN = 'your-telegram-bot-token'
    ```

5. Add `config.py` to `.gitignore` to ensure your token is not pushed to GitHub:

    ```plaintext
    # .gitignore
    config.py
    ```

6. Run the bot:

    ```bash
    python bot.py
    ```

## Running the Bot 24/7

To ensure the bot runs 24/7, you can deploy it on a cloud service like Heroku or AWS, or use a VPS.

---

# Телеграм-бот для отслеживания мата

Этот бот отслеживает использование матерных слов в чате Telegram. Он предоставляет статистику по количеству использованных матерных слов каждым участником и общему количеству матерных слов, использованных за день.

## Функции

- Отслеживание матерных слов в чате.
- Предоставление статистики для каждого участника.
- Предоставление ежедневной статистики для чата.

## Команды

- `/start` - Запустить бота и получить приветственное сообщение.
- `/help` - Показать информацию о командах.
- `/userstats` - Показать статистику матерных слов, использованных каждым участником.
- `/dailystats` - Показать ежедневную статистику матерных слов, использованных в чате.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/telegram-obscene-word-tracking-bot.git
    cd telegram-obscene-word-tracking-bot
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите необходимые пакеты:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `config.py` и добавьте в него ваш токен бота:

    ```python
    # config.py
    TOKEN = 'your-telegram-bot-token'
    ```

5. Добавьте `config.py` в `.gitignore`, чтобы ваш токен не попал в GitHub:

    ```plaintext
    # .gitignore
    config.py
    ```

6. Запустите бота:

    ```bash
    python bot.py
    ```

## Запуск бота 24/7

Чтобы бот работал 24/7, вы можете развернуть его на облачном сервисе, таком как Heroku или AWS, или использовать VPS.

