
import telebot
from telebot.util import content_type_media
from telebot import util

token = ""
bot = telebot.TeleBot(token)


# @bot.message_handler() => Used as a decoration, it is easier to read and provides direct customizations.
# bot.register_message_handler() => It provides an alternative way to register processors, which may be useful in certain situations.


# Usgs of rmh (register_message_handler)
#   If you need to register a message handler based on a specific condition or runtime state, 
#   register_message_handler() is more convenient. 
#   For example:
#     you can register a new handler based on user interaction or a special condition.



active = True

@bot.message_handler(commands=['s', 'h'])
def RCS(msg):
    bot.send_message(msg.chat.id, "A new msg command here.")

    if msg.text.startswith('/h'):
        bot.register_message_handler(doSomething, content_types=['photo'])


def doSomething(msg):
    bot.send_message(msg.chat.id, 1223733)





print("Bot Running Now ❤️")
bot.polling()

