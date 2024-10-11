
import telebot
from telebot.util import content_type_media
from telebot import util



token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"
bot = telebot.TeleBot(token)


# Handler Names Search
    # User Input was: /command name, age
    # If User Input Good Command return True if IN else False If not IN
        # /Command name, age

    # If User Input Bad Command return None
        # /Command 
        # /Command age name
        # /Command name
        # /Command age
        # /Command Wrong information => /Command blab blab blab blab ....


namesOlds = [
    {"name": "Ali Ahmed", "age": 30},
    {"name": "Hassan", "age": 25},
    {"name": "Hussain", "age": 40},
    {"name": "Mohammed Wissam", "age": 35},
    {"name": "Ja'far Khalid", "age": 28},
    {"name": "Musa", "age": 45},
    {"name": "Sajad Muslim", "age": 42},
    ]



@bot.message_handler(commands=['search'])
def handlerSearch(msg):
    ...



bot.polling()