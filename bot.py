import logging
import re
import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import checker, scripts

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

chat_stats = {}
daily_stats = {}

async def start(update: Update, context: CallbackContext) -> None:
    if update.message:
        await update.message.reply_text('Я отличный бот, я умею подсчитывать количество мата в чате')

async def help_command(update: Update, context: CallbackContext) -> None:
    if update.message:
        await update.message.reply_text('Команды:\n/start - начать\n/help - помощь\n/user_stats - статистика по участникам\n/daily_stats - статистика по дням')

async def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message:
        chat_id = update.message.chat_id
        user = update.message.from_user
        user_id = user.id
        user_name = user.full_name
        message_text = update.message.text

        if chat_id not in chat_stats:
            chat_stats[chat_id] = {}
        if user_id not in chat_stats[chat_id]:
            chat_stats[chat_id][user_id] = {'name': user_name, 'count': 0}
        words = re.split(r'[\s-]+', message_text)
        for word in words:
            if checker.is_word_obscene(word):
                chat_stats[chat_id][user_id]['count'] += 1

        current_date = datetime.datetime.now().date().isoformat()
        if chat_id not in daily_stats:
            daily_stats[chat_id] = {}
        if current_date not in daily_stats[chat_id]:
            daily_stats[chat_id][current_date] = 0
        for word in words:
            if checker.is_word_obscene(word):
                daily_stats[chat_id][current_date] += 1

async def user_stats_command(update: Update, context: CallbackContext) -> None:
    if update.message:
        chat_id = update.message.chat_id
        stats_message = "Статистика мата по участникам чата:\n"
        if chat_id in chat_stats:
            for user_id, data in chat_stats[chat_id].items():
                stats_message += f"{data['name']}: {data['count']} раз(а)\n"
        else:
            stats_message = "Нет данных для этого чата."
        await update.message.reply_text(stats_message)

async def daily_stats_command(update: Update, context: CallbackContext) -> None:
    if update.message:
        chat_id = update.message.chat_id
        stats_message = "Статистика мата по дням:\n"
        if chat_id in daily_stats:
            for date, count in daily_stats[chat_id].items():
                stats_message += f"{date}: {count} слов(а)\n"
        else:
            stats_message = "Нет данных для этого чата."
        await update.message.reply_text(stats_message)


def main() -> None:
    token = scripts.TOKEN
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("user_stats", user_stats_command))
    application.add_handler(CommandHandler("daily_stats", daily_stats_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
