from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_url_cats():
    contents = requests.get('https://some-random-api.ml/img/cat').json()
    url = contents['link']
    return url

def get_url_pandas():
    contents = requests.get('https://some-random-api.ml/img/panda').json()
    url = contents['link']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
        print(file_extension)
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def cat(bot, update):
    url = get_url_cats()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def panda(bot, update):
    url = get_url_pandas()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1035906504:AAHTStBWmmjkz-BIky-ZRtIJD90LYbSJL3A')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('cat', cat))
    dp.add_handler(CommandHandler('panda', panda))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



    # https://some-random-api.ml/