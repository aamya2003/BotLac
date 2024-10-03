import telebot

from telebot.util import content_type_media

token = "token"

bot = telebot.TeleBot(token)




@bot.message_handler(content_types=content_type_media)
def lis1(msg):
    print(msg)
    print(msg.id)
    print(msg.content_type)


print("Bot is Running")

bot.polling()






"""
'from_user': {
    'id': 7164500484,
      'is_bot': False,
        'first_name': '.', 
        'username': 'hshshn4', 
        'last_name': None, 
        'language_code': 'en', 
        'can_join_groups': None, 
        'can_read_all_group_messages': None,
          'supports_inline_queries': None,
            'is_premium': None,
              'added_to_attachment_menu': None,
                'can_connect_to_business': None,
                  'has_main_web_app': None}
"""