import telebot

from telebot.util import content_type_media

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)


# Send Message

    # 1- When Message Sent And Bot Is Active

    # 2- Send Message To Peer Chat


@bot.message_handler(content_types=content_type_media)
def handler(msg):
    bot.send_message(msg.chat.id, "مرحبا شكرا لارسال الرسالة.")



print("Bot is Running")
bot.polling()