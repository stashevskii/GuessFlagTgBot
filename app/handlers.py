from app.utils.utils import flags
from .keyboards import start_kb
from iso3166 import countries
from telebot import types

right_country_code = ''

def handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Hi 👋! Guess all flags and check your geography level!',
                         reply_markup=start_kb)

    @bot.message_handler(commands=['ban'])
    def answer(message):
        command_parts = message.text.split()

        if len(command_parts) > 1:
            if message.from_user.username == 'a100lex':
                banned = command_parts[1]
                with open('ban.txt', 'a') as f:
                    f.write(banned + '\n')
            else:
                bot.send_message(message, "You tried to hack. You will be banned!!!")
                with open('ban.txt', 'a') as f:
                    f.write(message.from_user.username + '\n')
        else:
            bot.send_message(message, "Give username to ban")

    @bot.message_handler(content_types=['text'])
    def quizz(message):
        global c, r, right_country_code
        if message.text == 'Start Quizz!':
            c = 0
            r = 0
            right_country_code = flags(message, 0, bot, True)
        if c == 9:
            if message.text == countries.get(right_country_code).name and message.text != 'Start Quizz!':
                r += 1
                bot.send_message(message.chat.id, 'Yeah!', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id, '🤗', reply_markup=types.ReplyKeyboardRemove())
            elif message.text != 'Start Quizz!':
                bot.send_message(message.chat.id, f'No! It is {countries.get(right_country_code).name}!',
                                 reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id, '😭', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, f'Your score is {r}/10!', reply_markup=start_kb)
        if c != 9:
            if message.text == countries.get(right_country_code).name and message.text != 'Start Quizz!':
                c += 1
                r += 1
                bot.send_message(message.chat.id, 'Yeah!', reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id, '🤗', reply_markup=types.ReplyKeyboardRemove())
                right_country_code = flags(message, c, bot)
            elif message.text != 'Start Quizz!':
                c += 1
                bot.send_message(message.chat.id, f'No! It is {countries.get(right_country_code).name}!',
                                 reply_markup=types.ReplyKeyboardRemove())
                bot.send_message(message.chat.id, '😭', reply_markup=types.ReplyKeyboardRemove())
                right_country_code = flags(message, c, bot)
