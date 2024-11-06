
import telebot

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"
bot = telebot.TeleBot(token)




# video
# You can send Video By various Ways

# 1- From your device
# 2- By File_id for video



# Caption
# you can titled you media by a name


file_id_video = "BAACAgIAAxkDAAID82crKIOnjoEY3AKr55WPHXlqMkYrAAJ9VgAC2PVYSUc6MiJ-HurlNgQ"

@bot.message_handler(commands=['video'])
def send_video_command(msg):
    # fm_  = bot.send_video(msg.chat.id, open("video.mp4", 'rb'), reply_to_message_id=msg.id, caption="blbalsaiosd")

    # print(fm_.video.file_id)

    bot.send_video(msg.chat.id,video= file_id_video, caption='7dud')



@bot.message_handler(chat_types=['group', 'supergroup'], commands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, "This Bot Can send you video!", reply_to_message_id=msg.id)



print("Bot Running Now ❤️")
bot.polling()

