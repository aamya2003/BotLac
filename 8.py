import telebot

from telebot.util import content_type_media

token = "token"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=content_type_media)
def lis1(msg):
    print("A new message")







print("Bot is Running")
bot.polling()