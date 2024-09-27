import telebot

token = "ضع التوكن الخاص بك هنا"

bot = telebot.TeleBot(token)



BotInfo = bot.get_me()

print(BotInfo.first_name)
