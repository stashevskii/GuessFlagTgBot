from iso3166 import countries
from ..keyboards import choose_pos_for_right_flag
import random
import os

right_country_code = ''

def flags(message, count, bot, flag=False):
    global right_country_code
    country_codes = []
    for i in range(3):
        filename = random.choice(os.listdir('flags'))
        code = countries.get(filename.split('.')[0]).name
        country_codes.append(code)
    filename = random.choice(os.listdir('flags'))
    right_country_code = filename.split('.')[0]
    path = os.path.join('flags', filename)

    rk = choose_pos_for_right_flag(country_codes, count, right_country_code, flag)

    flag = open(path, 'rb')
    bot.send_photo(message.chat.id, photo=flag, reply_markup=rk)

    return right_country_code
