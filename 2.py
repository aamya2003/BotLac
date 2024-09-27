import telebot

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)



BotInfo = bot.get_me()

print(BotInfo.first_name)
