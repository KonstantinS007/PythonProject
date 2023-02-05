#  .\scriptbot.py
import telebot
from telebot import types

with open('../../../Cat.txt', 'r') as f:
    cat = f.read()

bot = telebot.TeleBot(cat)


@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Текст", url='https://habr.com')
    markup.add(button1)
    bot.send_message(message.chat.id, "на кнопку".format(message.from_user), reply_markup=markup)




bot.polling()
