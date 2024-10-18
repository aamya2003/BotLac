
import telebot

token = ""
bot = telebot.TeleBot(token)


# Body mass index (BMI)
""" is a value derived from the mass (weight) and height of a person.
    The BMI is defined as the body mass divided by the square of the body height
    , and is expressed in units of kg/m2, resulting from mass in kilograms (kg) and height in metres (m)."""


# --- The BMI is a convenient rule of thumb used to broadly categorize a person as based on tissue mass (muscle, fat, and bone) and height 


"""

BMI = M / H^2

M in kg
H in m

100 cm = 1 m
"""

# Normal range (BMI) => 18.5   – 24.9
#                       normal - ideal

# Convert height cm to meter by => height * 10^-2


@bot.message_handler(commands=['bmi'])
def handler_bmi(msg):
    bot.send_message(msg.chat.id, "ارسل طولك: ")
    bot.register_next_step_handler(msg, handler_height)


def handler_height(msg):
    text = msg.text
    if text.isnumeric():
        height = int(text)
        bot.send_message(msg.chat.id, "ارسل وزنك: ")
        bot.register_next_step_handler(msg, handler_weight, height)


def handler_weight(msg, height):
    text = msg.text
    if text.isnumeric():
        weight = int(text)
        height_m = height / 100

        bmi = weight / height_m**2

        if bmi <= 18.4:
            bot.send_message(msg.chat.id, "لديك نقص حاد في وزنك")
        
        elif 18.5 <= bmi <= 24.9:
            bot.send_message(msg.chat.id, "وزنك طبيعي")
        
        elif bmi >= 25:
            bot.send_message(msg.chat.id, "لديك سمنه مفرطة")
        
            



print("Bot Running Now ❤️")
bot.polling()

