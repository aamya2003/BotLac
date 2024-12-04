
import telebot

token = ""
bot = telebot.TeleBot(token)


# Media
# 1- photo
# 2- vedio
# 3- audio
# 4- voice
# 5- sticker
# 6- animation
# 7- video_note
# 8- document



@bot.message_handler(commands=['video', 'vid'])
def send_video_command(msg):
    bot.send_video(msg.chat.id,video= open("video.mp4", 'rb'), caption='هذا الفيديو المفضل لدي ✨.')


@bot.message_handler(commands=['photo', 'ph'])
def send_photo_command(msg):
    bot.send_video(msg.chat.id,video= open("child.jpg", 'rb'), caption="انا احب هذه الصورة.")


@bot.message_handler(commands=['audio', 'a'])
def send_audio_command(msg):
    bot.send_audio(msg.chat.id,audio= open("audio.mp3", 'rb'), caption="انا احب هذه النغمة.")


@bot.message_handler(commands=['voice', 'vc'])
def send_voice_command(msg):
    bot.send_voice(msg.chat.id,voice= open("audio.mp3", 'rb'), caption="انا احب هذه الرنة.")

@bot.message_handler(commands=['sticker', 'sic'])
def send_sticker_command(msg):
    bot.send_sticker(msg.chat.id,sticker= open("stick.webp", 'rb'))

@bot.message_handler(commands=['anim', 'am'])
def send_anim_command(msg):
    bot.send_animation(msg.chat.id,animation= open("anim.mp4", 'rb'), caption="انا احب هذا الانميشين.")

@bot.message_handler(commands=['doc'])
def send_doc_command(msg):
    bot.send_document(msg.chat.id,document= open("11.py", 'rb'), caption="انا احب هذا المستند.")



@bot.message_handler(commands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, "This Bot Can send you media!", reply_to_message_id=msg.id)



print("Bot Running Now ❤️")
bot.polling()

