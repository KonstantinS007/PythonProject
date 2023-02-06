#          botele.py
import telebot

from extensions import ConvertionException, CryptoConverter
from config import keys
from config import TOKEN

# Создали объект bot
bot = telebot.TeleBot(TOKEN)
# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.


@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n \
<имя валюты цену которой хотите узнать> \n \
<имя валюты в которой надо узнать цену первой валюты> \n \
<количество переводимой валюты>\n доллар рубль 1 - пример ввода\nУвидеть список всех доступных валют: /values'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in keys.keys():
        text = ' / '.join((text, key,))
    bot.reply_to(message, text + ' /')


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Неверные параметры.')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя./help:\n{e}')
        # with open('1227436.jpg', 'rb') as f:
        #     img = f.read()
        # bot.send_photo(message.chat.id, img)
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду:\n{e}')
        # with open('44334231.jpg', 'rb') as f:
        #     img = f.read()
        # bot.send_photo(message.chat.id, img)

    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
