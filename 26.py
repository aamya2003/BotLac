
import telebot

token = ""
bot = telebot.TeleBot(token)




# photo
# You can send Photo By various Ways

# 1- By url link
# 2- from your device
# 3- By File id for photo



@bot.message_handler( commands=['photo'])
def set_name_handler(msg):
    # bot.send_photo(msg.chat.id, "https://t3.ftcdn.net/jpg/00/55/28/74/240_F_55287480_SBLT6xLnVhJ1u5Ek5DqpKtlwxeRb4UAM.jpg", reply_to_message_id=msg.id)
    # bot.send_photo(msg.chat.id, photo=open("child.jpg", "rb"), reply_to_message_id=msg.id)
    bot.send_photo(msg.chat.id, photo="AgACAgIAAyEFAASPTI05AAIBlGckZiEoMipRrGz_twgktNi6pFNrAAKM4jEb4KIgSaTXoN-AZ1qLAQADAgADeAADNgQ", reply_to_message_id=msg.id)




@bot.message_handler(chat_types=['group', 'supergroup'], commands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, "Start msg", reply_to_message_id=msg.id)



@bot.message_handler(content_types=['photo'])
def start_handler(msg):
    photo_1 = msg.photo[-1]
    print(photo_1.file_id)
    if "AgACAgIAAyEFAASPTI05AAIBlGckZiEoMipRrGz_twgktNi6pFNrAAKM4jEb4KIgSaTXoN-AZ1qLAQADAgADeAADNgQ" == photo_1.file_id:
        print(True)




print("Bot Running Now ❤️")
bot.polling()