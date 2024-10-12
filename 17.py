
import telebot
from telebot.util import content_type_media
from telebot import util



token = ""
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




correctForm = "/search name, age"

"/s"

UserInputs = "name, age"

# x = ['name', 'age']


# x = ['ahmed', 'ahmed']

# x1 = x[0]
# x2 = x[1]


# print(x1.isalpha())
# print(x2.isnumeric())


@bot.message_handler(commands=['search', 's'])
def hanlderSearch(msg):
    args = util.extract_arguments(msg.text)
    # If Msg Not Empty
    if args != "":
        data = args.split(", ")
        # If User Interd Good Form
        if len(data) == 2:
            elm1 = data[0]
            elm2 = data[1]
            # IF User Enter name, age Good
            if elm1.isalpha() and elm2.isnumeric():
                # Convert Age(str) To Age(num)
                elm2 = int(elm2)
                # Show Dic in names list
                checked = None
                for diCi in namesOlds:
                    name = diCi['name']
                    age = diCi["age"]
                    # Vertfy If User searched is found in list name 
                    if name == elm1 and age == elm2:
                        bot.send_message(msg.chat.id, "User Found.")
                        checked = True
                        break
                # IF Searched data not in names list
                if checked == None:
                    bot.send_message(msg.chat.id, "User Not Found!")

            else:
                print("Bad Form")

        else:
            print("Bad")

    else:
        print("Msg Is Empty")










print("Bot Running Now ❤️")
bot.polling()