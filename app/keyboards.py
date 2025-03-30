from iso3166 import countries
from telebot import types
import random

kbs = []


def choose_pos_for_right_flag(codes, counter, right_country_code, flag=False):
    global kbs
    if flag:
        kbs = []
    num = random.randint(0, 3)
    kbs.append(types.ReplyKeyboardMarkup(True))
    if num == 0:
        kbs[counter].row(countries.get(right_country_code).name, codes[0])
        kbs[counter].row(codes[1], codes[2])
    elif num == 1:
        kbs[counter].row(codes[0], countries.get(right_country_code).name)
        kbs[counter].row(codes[1], codes[2])
    elif num == 2:
        kbs[counter].row(codes[0], codes[1])
        kbs[counter].row(countries.get(right_country_code).name, codes[2])
    elif num == 3:
        kbs[counter].row(codes[0], codes[1])
        kbs[counter].row(codes[2], countries.get(right_country_code).name)

    return kbs[counter]


start_kb = types.ReplyKeyboardMarkup(True)
start_kb.row('Start Quizz!')
