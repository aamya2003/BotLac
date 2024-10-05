import telebot

from telebot.util import content_type_media

token = "token"

bot = telebot.TeleBot(token)


# Send Message

    # 1- When Message Sent And Bot Is Active

    # 2- Send Message To Peer Chat


bot.send_message(chat_id=7164500484, text="ارسلت لك رسالة لانك قد قلت لي ارسل الي رسالة.")


# https://t.me/myidbot


print("Bot is Running")
bot.polling()