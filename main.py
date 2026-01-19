import telebot
import token

bot = telebot.TeleBot('8518348143:AAGvAyjZTutpB8Hx6rDPR5medR_WshPaKB4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот. Чем могу помочь?')

bot.polling(none_stop=True, interval=0)