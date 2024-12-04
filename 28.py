
import telebot

token = ""
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['video'])
def send_video_command(msg):
    bot.send_video(msg.chat.id,video= open("video.mp4", 'rb'), caption='هذا الفيديو المفضل لدي ✨.')


@bot.message_handler(commands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, "This Bot Can send you media!", reply_to_message_id=msg.id)



print("Bot Running Now ❤️")
bot.polling()

