import telebot

from telebot.util import content_type_media

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=content_type_media)
def lis1(msg):
    print(msg.from_user)







print("Bot is Running")
bot.polling()