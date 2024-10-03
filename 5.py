import telebot


token = "token"

bot = telebot.TeleBot(token)


@bot.message_handler()
def lis1(msg):
    print(msg)

print("Bot is Running")
bot.polling()