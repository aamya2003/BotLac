import telebot
from telebot.handler_backends import ContinueHandling


token = "token"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["photo", "text", "voice"], )
def lis1(msg):
    print("A new message 1")



@bot.message_handler(content_types=["animation"])
def lis2(msg):
    print("A new message 2")




print("Bot is Running")
bot.polling()