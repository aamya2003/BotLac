
import telebot

token = ""
bot = telebot.TeleBot(token)



# reply_to_message

# Not None if message is replied 
# Else None 

# To delete A message
# To reply message
# To get info message
# To do something
# To handle with a specific message


box = ['a1', 'z', 'Hi mr']


@bot.message_handler()
def handler(msg):
    bot.send_message(msg.chat.id, "Hi mr")


    msg.text

    if msg.reply_to_message:
        print()
        msg_ = msg.reply_to_message 
        print(msg_.text)


    msg_ = msg.reply_to_message 
    if msg_:
        text = msg_.text

        if text in box:
            bot.delete_message(msg.chat.id, message_id=msg_.id)





print("Bot Running Now ❤️")
bot.polling()

