import telebot
from telebot.util import content_type_media
token = ""
bot = telebot.TeleBot(token)


# Message Text Type
    # 1- Commmand
    # 2- Status
    # 3- Any Text



@bot.message_handler(commands=['start', 'help', 'id'])
def handler1(msg):
    bot.send_message(msg.chat.id, "انت ارسلت رسالة امرية")



@bot.message_handler(regexp=r'age = [0-9]{1,3}$')
def handler2(msg):
    bot.send_message(msg.chat.id, "انت ادخلت تعبيرا")



@bot.message_handler(content_types=['text'])
def handler3(msg):
    bot.send_message(msg.chat.id, "مرحبا شكرا لارسال الرسالة.")


# @bot.message_handler(content_types=['text'])
# def handler4(msg):
#     bot.send_message(msg.chat.id, "مرحبا شكرا لارسال msg.")


print("Bot is Running")
bot.polling()