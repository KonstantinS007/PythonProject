#  .\scriptbot.py
import telebot

with open('../../../Cat.txt', 'r') as f:
   cat = f.read()

bot = telebot.TeleBot(cat)


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f"Welcome, {message.chat.username}")


bot.polling(none_stop=True)
