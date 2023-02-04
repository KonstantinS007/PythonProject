#           BOT_MAIN.PY
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
<имя валюты цену которой хотите узнать> \
<имя валюты в которой надо узнать цену первой валюты> \
<количество переводимой валюты>\n Увидеть список всех доступных валют: /values'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}, понял какашка'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
