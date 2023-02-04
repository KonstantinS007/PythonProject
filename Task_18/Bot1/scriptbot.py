#  .\scriptbot.py
import telebot

with open('../../../Cat.txt', 'r') as f:
    cat = f.read()

bot = telebot.TeleBot(cat)


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f"Ёжик вреднёжик, {message.chat.username}")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
