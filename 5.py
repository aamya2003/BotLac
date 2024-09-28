import telebot


token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)


@bot.message_handler()
def lis1(msg):
    print(msg)

print("Bot is Running")
bot.polling()