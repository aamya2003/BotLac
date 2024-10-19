
import telebot

token = ""
bot = telebot.TeleBot(token)



# message_id

# reply_to_message
# edit message text | edit_message_media
# delete message
# ....


@bot.message_handler()
def handler(msg):
    # bot.send_message(msg.chat.id, "Hi Mr.", reply_to_message_id=msg.id)
    # bot.reply_to(msg, "Hi Mr." )


    # bot.delete_message(msg.chat.id, msg.id)


    # bot.edit_message_text("FFUfe", msg.chat.id, msg.id)

    # bot.edit_message_media(chat_id=929921, message_id=msg.id, media=)

    bot.send_message(msg.chat.id, "bbdvviusdvi",reply_to_message_id=804 )

    print(msg.id)


print("Bot Running Now ❤️")
bot.polling()

