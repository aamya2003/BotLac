
import telebot

token = ""
bot = telebot.TeleBot(token)



class usS:
    name_value = 1

users_status = {}


@bot.message_handler(chat_types=['group', 'supergroup'], commands=['set_my_name'])
def set_name_handler(msg):
    bot.send_message(msg.chat.id, "Send your name", reply_to_message_id=msg.id)
    users_status[msg.from_user.id] = usS.name_value



@bot.message_handler(chat_types=['group', 'supergroup'], commands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, "Start msg", reply_to_message_id=msg.id)


def name_f_f(msg):
    if users_status.get(msg.from_user.id) == usS.name_value:
        return True
    


@bot.message_handler(func=name_f_f)
def user_name_value(msg):
    bot.send_message(msg.chat.id, "Thanks", reply_to_message_id=msg.id)
    bot.send_message(msg.chat.id, f"You name is: {msg.text}", reply_to_message_id=msg.id)



# def user_name_value(msg, usid):
#     # Msg
#     if usid == msg.from_user.id:
#         bot.send_message(msg.chat.id, "Thanks", reply_to_message_id=msg.id)
#         bot.send_message(msg.chat.id, f"You name is: {msg.text}", reply_to_message_id=msg.id)

#     else:
#         bot.register_next_step_handler(msg, user_name_value, usid)


print("Bot Running Now ❤️")
bot.polling()