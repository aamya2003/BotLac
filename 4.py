import telebot


token = "token"

bot = telebot.TeleBot(token)




print("Bot is Running")
bot.polling()