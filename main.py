import json
import os
import telebot
import dotenv
from telebot import types

dotenv.load_dotenv()

bot = telebot.TeleBot(os.environ.get('BOT_KEY'))


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'И тебе здарова', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('morzh_4sv.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Внятно говори, ёпта', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'wow such shitty photo')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Ходь сюды', url='https://www.google.com/'))
    bot.send_message(message.chat.id, 'such original', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('гугол')
    start = types.KeyboardButton('старт')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'such original', reply_markup=markup)


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Репозиторий этого прекрасного поставщина моржей")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


# команда выше рисует кнопку с текстом кнопка
# читаем любой текст (включая кнопку)
# если текст == кнопка, то отправляем сообщение, затем создаем вторую кнопку
# при нажатии на вторую кнопку - рекурсия и новый текст
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Репозиторий этого прекрасного поставщина моржей":
        bot.send_message(message.chat.id, "https://github.com/Borteq2")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Тоже какая-то интересная кнопка")
        markup.add(item1)
        bot.send_message(message.chat.id, 'А это тут зачем?', reply_markup=markup)
    elif message.text == "Тоже какая-то интересная кнопка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        refresh = types.KeyboardButton('/button')
        markup.add(refresh)
        bot.send_message(message.chat.id, 'Запустить заново', reply_markup=markup)


bot.polling(none_stop=True)
