import telebot

from telebot.util import content_type_media

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=content_type_media)
def lis1(msg):
    inf = f"""
The Msg Info:
    1- content type = {msg.content_type}
    2- msg id = {msg.id}
    3- msg date = {msg.date}

The User Info:
    1- username = {msg.from_user.username}
    2- first name = {msg.from_user.first_name}
    3- last name = {msg.from_user.last_name}
    4- user id = {msg.from_user.id}


The Chat Info:
    1- chat type = {msg.chat.type}
    2- chat first name = {msg.chat.first_name}
    3- chat id = {msg.chat.id}
"""
    print(inf)










print("Bot is Running")

bot.polling()