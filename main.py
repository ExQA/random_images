from telegram import bot
import telebot
from telebot import types
import requests
import re


def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_url_cats():
    contents = requests.get('https://some-random-api.ml/img/cat').json()
    url = contents['link']
    return url


def get_url_panda():
    contents = requests.get('https://some-random-api.ml/img/panda').json()
    url = contents['link']
    return url


def get_url_red_panda():
    content = requests.get('https://some-random-api.ml/img/red_panda').json()
    url = content['link']
    return url


def get_url_fox():
    content = requests.get('https://some-random-api.ml/img/fox').json()
    url = content['link']
    return url


def get_url_koala():
    content = requests.get('https://some-random-api.ml/img/koala').json()
    url = content['link']
    return url


def get_image_dog():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url_dog()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
        print(file_extension)
    return url


token = '1035906504:AAHTStBWmmjkz-BIky-ZRtIJD90LYbSJL3A'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    cat_button = types.InlineKeyboardButton(text='Cat', callback_data='cat')
    dog_button = types.InlineKeyboardButton(text='Dog', callback_data='dog')
    panda_button = types.InlineKeyboardButton(text='Panda', callback_data='panda')
    red_panda_button = types.InlineKeyboardButton(text='Red Panda', callback_data='red_panda')
    koala_button = types.InlineKeyboardButton(text='Koala', callback_data='koala')
    fox_button = types.InlineKeyboardButton(text='Fox', callback_data='fox')
    key.add(cat_button, dog_button, panda_button, red_panda_button, fox_button, koala_button)
    bot.send_message(message.chat.id, 'Select your pat', reply_markup=key)
    print(message)


@bot.callback_query_handler(func=lambda c: True)
def answer(c):
    key = types.InlineKeyboardMarkup()
    cat_button = types.InlineKeyboardButton(text='Cat', callback_data='cat')
    dog_button = types.InlineKeyboardButton(text='Dog', callback_data='dog')
    panda_button = types.InlineKeyboardButton(text='Panda', callback_data='panda')
    red_panda_button = types.InlineKeyboardButton(text='Red Panda', callback_data='red_panda')
    koala_button = types.InlineKeyboardButton(text='Koala', callback_data='koala')
    fox_button = types.InlineKeyboardButton(text='Fox', callback_data='fox')
    key.add(cat_button, dog_button, panda_button, red_panda_button, fox_button, koala_button)

    if c.data == 'cat':
        bot.send_photo(c.message.chat.id, photo=get_url_cats())
        bot.send_message(c.message.chat.id, 'Select your pat', reply_markup=key)
    elif c.data == 'dog':
        bot.send_photo(c.message.chat.id, photo=get_image_dog())
        bot.send_message(c.message.chat.id, 'Select your pat', reply_markup=key)
    elif c.data == 'panda':
        bot.send_photo(c.message.chat.id, photo=get_url_panda())
        bot.send_message(c.message.chat.id, 'Select your pat', reply_markup=key)
    elif c.data == 'red_panda':
        bot.send_photo(c.message.chat.id, photo=get_url_red_panda())
        bot.send_message(c.message.chat.id, 'Select your pat', reply_markup=key)
    elif c.data == 'fox':
        bot.send_photo(c.message.chat.id, photo=get_url_fox())
        bot.send_message(c.message.chat.id, 'Select your pat', reply_markup=key)
    elif c.data == 'koala':
        bot.send_photo(c.message.chat.id, photo=get_url_koala())
        bot.send_message(c.message.chat.id, 'Select your pat', reply_markup=key)


if __name__ == '__main__':
    bot.polling(none_stop=True)

    # https://some-random-api.ml/
