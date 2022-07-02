import telebot
from auth_info import bot_token, client_user_id

bot = telebot.TeleBot(bot_token)
bot_name = f"@{bot.get_me().username}"

def sent_msg2bot(txt):
    #function for sending message to the user
    try:
        @bot.message_handler(content_types=['text'])
        def get_text_message(message):
            bot.send_message(client_user_id, txt)
        get_text_message('send')
    except:
        pass
