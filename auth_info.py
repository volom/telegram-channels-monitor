# input info from https://my.telegram.org/
from telethon import TelegramClient, events, sync

#telegram client
session_name = 'scraper'
api_id = 11111111
api_hash = 'api_hash'

# telegram bot
bot_token = 'bot_token'

client = TelegramClient(session_name, api_id, api_hash)
client.start()

# get user id of the client
client_user_id = client.get_me().id
