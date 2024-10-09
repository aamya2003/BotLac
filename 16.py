



import telebot
from telebot.util import content_type_media

from telebot import util

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start', 'help'])
def handlerCommandStart(msg):
    bot.send_message(msg.chat.id, "This Bot For Helping You, Have A nice Try!")




@bot.message_handler(commands=['gt_myid'])
def handlerId(msg):
    bot.send_message(msg.chat.id, msg.from_user.id)




@bot.message_handler(commands=['calc_a'])
def handlerCArea(msg):
    # print(msg.text)
    args = util.extract_arguments(msg.text)
    new_args = args.split(" ")
    # print(new_args)
    x = int(new_args[0])
    y = int(new_args[1])
    result = x * y
    # print(result)
    bot.send_message(msg.chat.id, result)




bot.polling()







# x = "10 20"

# y = "ahmed 2023/11/11 10:20"


# new_x = x.split(" ")

# new_y = y.split(" ")

# print(new_x[1])
# print(new_y[2])