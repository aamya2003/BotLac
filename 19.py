
import telebot

token = ""
bot = telebot.TeleBot(token)


#### register_next_step_handler || register_message_handler

# => When We Need To Run A handler For Ever We use register_message_handler
# => When We Need To Run A handler For A spiscfic event We use register_next_step_handler


# => When We Run A handler using register_message_handler The rest functions won't sleep 
# => When We Run A handler using register_next_step_handler The rest functions will sleep until a specific condition executed



# In General Form

# @bot.....()
# def ...(msg):
    # cond
        # run a function

# def ...(msg):
    # code





@bot.message_handler(commands=['s1', 's2'])
def message_handler(msg):
    if msg.text.startswith("/s1"):
        bot.send_message(msg.chat.id, "Hi, How Can I Help You?")

    elif msg.text.startswith("/s2"):
        bot.send_message(msg.chat.id, "A handler run...")
        bot.register_next_step_handler(msg, hanlder_)



def hanlder_(msg):
    if msg.content_type == "photo":
        bot.send_message(msg.chat.id, "A New Photo Shared!")

    else:
        bot.register_next_step_handler(msg, hanlder_)










print("Bot Running Now ❤️")
bot.polling()