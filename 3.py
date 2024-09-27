import telebot

token = "7515698207:AAH8vxp3bTLzpkMfb4g_l0cuURiQ4cEbA2Q"

bot = telebot.TeleBot(token)



@bot.message_handler()
def msgsHandler(msg):
    print(msg.content_type)




bot.polling()

"""
{
  "content_type": "text",
  "id": 5,
  "message_id": 5,
  "from_user": {
    "id": 7164500484,
    "is_bot": false,
    "first_name": ".",
    "username": "hshshn4",
    "last_name": null,
    "language_code": "en",
    "can_join_groups": null,
    "can_read_all_group_messages": null,
    "supports_inline_queries": null,
    "is_premium": null,
    "added_to_attachment_menu": null,
    "can_connect_to_business": null,
    "has_main_web_app": null
  },
  "date": 1727420299,
  "chat": {
    "id": 7164500484,
    "type": "private",
    "title": null,
    "username": "hshshn4",
    "first_name": ".",
    "last_name": null,
    "is_forum": null,
    "max_reaction_count": null,
    "photo": null,
    "bio": null,
    "join_to_send_messages": null,
    "join_by_request": null,
    "has_private_forwards": null,
    "has_restricted_voice_and_video_messages": null,
    "description": null,
    "invite_link": null,
    "pinned_message": null,
    "permissions": null,
    "slow_mode_delay": null,
    "message_auto_delete_time": null,
    "has_protected_content": null,
    "sticker_set_name": null,
    "can_set_sticker_set": null,
    "linked_chat_id": null,
    "location": null,
    "active_usernames": null,
    "emoji_status_custom_emoji_id": null,
    "has_hidden_members": null,
    "has_aggressive_anti_spam_enabled": null,
    "emoji_status_expiration_date": null,
    "available_reactions": null,
    "accent_color_id": null,
    "background_custom_emoji_id": null,
    "profile_accent_color_id": null,
    "profile_background_custom_emoji_id": null,
    "has_visible_history": null,
    "unrestrict_boost_count": null,
    "custom_emoji_sticker_set_name": null,
    "business_intro": null,
    "business_location": null,
    "business_opening_hours": null,
    "personal_chat": null,
    "birthdate": null,
    "can_send_paid_media": null
  },
  "text": "السلام عليكم",
  "json": {
    "message_id": 5,
    "from": {
      "id": 7164500484,
      "is_bot": false,
      "first_name": ".",
      "username": "hshshn4",
      "language_code": "en"
    },
    "chat": {
      "id": 7164500484,
      "first_name": ".",
      "username": "hshshn4",
      "type": "private"
    },
    "date": 1727420299,
    "text": "السلام عليكم"
  }
}
"""



