import telebot

from telebot.util import content_type_media

token = "token"

bot = telebot.TeleBot(token)




@bot.message_handler(content_types=content_type_media)
def lis1(msg):
    print(msg.from_user)
    print(msg.from_user.first_name)
    print(msg.from_user.username)



print("Bot is Running")

bot.polling()