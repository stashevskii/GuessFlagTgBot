from app.handlers import handlers
from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()
bot = TeleBot(os.getenv("TOKEN"))
handlers(bot)

bot.polling(none_stop=True, interval=0)
