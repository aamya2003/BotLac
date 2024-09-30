import telebot
from telebot.handler_backends import ContinueHandling

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)


@bot.message_handler()
def lis1(msg):
    print(f"1")
    return ContinueHandling()



@bot.message_handler()
def lis2(msg):
    print(f"2")





print("Bot is Running")
bot.polling()