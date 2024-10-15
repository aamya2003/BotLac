
import telebot

token = ""
bot = telebot.TeleBot(token)




#<=> register_next_step_handler <=>
# => It's useful when you need to split a conversation with the user into multiple steps.
# =>This function helps you handle the next messages from the user after one step is executed.


## How Is It Work?
# ----When using register_next_step_handler:
#      1-  the current function is `suspended`
#      2- and a specific function `is registered to be called` when the user sends their next message.


# Send /sv
# Send your name
# send myname 
# Send your age
# send myage
# your data is ....



@bot.message_handler(commands=['sv'])
def HandlerSv(msg):
    bot.send_message(msg.chat.id, "Send Your name: ")
    bot.register_next_step_handler(msg, HandlerName)


def HandlerName(msg):
    if msg.text.startswith("/sv"):
        HandlerSv(msg)
    else:
        bot.send_message(msg.chat.id, "Send Your age: ")
        bot.register_next_step_handler(msg, HandlerAge, msg.text)


    
def HandlerAge(msg, name):
    if msg.text.startswith("/sv"):
        HandlerSv(msg)
    else:
        bot.send_message(msg.chat.id, f"Done, Your name is {name}, and your age is {msg.text}")


    


print("Bot Running Now ❤️")
bot.polling()

