
import telebot

token = ""
bot = telebot.TeleBot(token)



# Filters
# The function of filters in Telegram bots 
#     is to identify and process messages or services 
#     that the bot should deal with that meet certain conditions.

# Usage
# 1 - Create handler
# 2- Put func = Filter_function as pram in handler
# You Can Use Python's Class 

"""
def filter_func(msg):
    condition
    return True or False
"""
"""
class class_name:
    variable = value
    ... = ...
"""


class checked:
    start = 0


def myFilter(msg):
    return checked.start


@bot.message_handler(commands=['s', 'a'])
def some_handler(msg):
    bot.send_message(msg.chat.id, "something mesaage")

    if msg.text.startswith('/s'):
        checked.start = 1

    
    if msg.text.startswith('/a'):
        checked.start = 0



@bot.message_handler(func=myFilter)
def some_filter(msg):
    bot.send_message(msg.chat.id, "something my filter")



print("Bot Running Now ❤️")
bot.polling()