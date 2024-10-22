
import telebot

token = ""
bot = telebot.TeleBot(token)


# forward_from
# get msg data from private forward


# forward_origin
# get msg data from all 


@bot.message_handler()
def forward_handler(msg):
    # print(msg.forward_origin)

    if msg.forward_origin:
        print(msg.forward_origin.sender_user.id)



print("Bot Running Now ❤️")
bot.polling()