import telebot

token = "token"

bot = telebot.TeleBot(token)



BotInfo = bot.get_me()

print(BotInfo.first_name)
