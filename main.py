import os

import telebot
from telebot import types
from dotenv import load_dotenv
from apps.intro import Start, Info, Help
from apps.questions import question1, question2, question3, question4, question5
from apps.test import First_sym, Second_sym, Third_sym, Fourth_sym, Fith_sym
from apps.result import Result

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'restart', 'перезагрузка'])
def send_welcome(message):
    text = Start().greet()
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('/инструкция')
    bt2 = types.KeyboardButton('/оценить')
    markup.row(bt1, bt2)
    bt3 = types.KeyboardButton('/помощь')
    bt4 = types.KeyboardButton('/перезагрузка')
    markup.row(bt3, bt4)
    bot.send_message(message.chat.id, f"{text}", reply_markup=markup)


@bot.message_handler(commands=['инструкция'])
def get_info(message):
    text = Info().instruction()
    bot.send_message(message.chat.id, f"{text}", parse_mode='html')


@bot.message_handler(commands=['помощь'])
def send_welcome(message):
    text = Help.get_help()
    bot.send_message(message.chat.id, f"{text}", parse_mode='html')


@bot.message_handler(commands=['gettest', 'back', 'оценить'])
def get_ask(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bt1 = types.KeyboardButton('0')
    bt2 = types.KeyboardButton('1')
    bt3 = types.KeyboardButton('2')
    markup.row(bt1, bt2, bt3)
    # markup.add(types.InlineKeyboardButton('/back'))
    bot.send_message(message.chat.id, question1, reply_markup=markup)
    bot.register_next_step_handler(message, ask1)


def ask1(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bt1 = types.KeyboardButton('0')
    bt2 = types.KeyboardButton('1')
    bt3 = types.KeyboardButton('2')
    markup.row(bt1, bt2, bt3)
    # markup.add(types.InlineKeyboardButton('/back'))
    the_sum = message.text
    First_sym().thorax_symptoms(the_sum)
    bot.send_message(message.chat.id, question2, reply_markup=markup)
    bot.register_next_step_handler(message, ask2)


def ask2(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bt1 = types.KeyboardButton('0')
    bt2 = types.KeyboardButton('1')
    bt3 = types.KeyboardButton('2')
    markup.row(bt1, bt2, bt3)
    the_sum = message.text
    Second_sym().riber_symptoms(the_sum)
    bot.send_message(message.chat.id, question3, reply_markup=markup)
    bot.register_next_step_handler(message, ask3)


def ask3(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bt1 = types.KeyboardButton('0')
    bt2 = types.KeyboardButton('1')
    bt3 = types.KeyboardButton('2')
    markup.row(bt1, bt2, bt3)
    the_sum = message.text
    Third_sym().xiphoid_symptoms(the_sum)
    bot.send_message(message.chat.id, question4, reply_markup=markup)
    bot.register_next_step_handler(message, ask4)


def ask4(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bt1 = types.KeyboardButton('0')
    bt2 = types.KeyboardButton('1')
    bt3 = types.KeyboardButton('2')
    markup.row(bt1, bt2, bt3)
    the_sum = message.text
    Fourth_sym().mandibula_symptoms(the_sum)
    bot.send_message(message.chat.id, question5, reply_markup=markup)
    bot.register_next_step_handler(message, ask5)


def ask5(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('/инструкция')
    bt2 = types.KeyboardButton('/оценить')
    markup.row(bt1, bt2)
    bt3 = types.KeyboardButton('/помощь')
    bt4 = types.KeyboardButton('/перезагрузка')
    markup.row(bt3, bt4)
    the_sum = message.text
    Fith_sym().breath_symptoms(the_sum)
    result = Result().get_result()
    bot.send_message(message.chat.id, result, reply_markup=markup)


bot.polling(non_stop=True)
