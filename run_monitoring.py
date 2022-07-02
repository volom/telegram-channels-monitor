from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerEmpty
from auth_info import *
from bot_send_message import *
import re
import time
from itertools import compress


# choose channels to monitor. Set names
monitoring_channels = ['channel_name1', 'channel_name2', 'channel_name3',
                       'channel_name4', 'channel_name5']
# choose key words for fetching messages
key_words = ["keyword1", "keyword2", "keyword3", "keyword4"]

# set time pause for refreshing requests (in seconds)
time_pause = 60

# set limit of messages amount
limit_msg = 3


# preprocess key words
key_words = [x.lower() for x in key_words]
key_words = [re.sub(r'\s+', ' ', x) for x in key_words]

def check_key_msg(msg, kw):
    # function for checking if message contains at least one of the key words
    msg = msg.lower()
    msg = re.sub(r'\s+', ' ', msg).strip(" ")

    return any(s in msg for s in kw), ', '.join(list(compress(kw, [s in msg for s in kw])))


chats = []
last_date = None

groups = [] 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=100000,
             hash = 0
         ))
chats.extend(result.chats)

def notify_user(key_word, channel_name, msg_id, chat_id):
    #function for forwarding message from channel to telegram bot and sending message from bot to the user
    sent_msg2bot(f"key words: {key_word}, channel name: {channel_name}")
    client.forward_messages(bot_name, msg_id, chat_id)

for chat in chats:
    try:
        groups.append(chat)
    except:
        continue

def main():
    all_msg = []
    while True:
        for target_group in groups:
            if target_group.title in monitoring_channels:
                channel_entity=client.get_entity(target_group.title)
                posts = client(GetHistoryRequest(
                    peer=channel_entity,
                    limit=limit_msg,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0))

                post_msg = posts.messages
                
                for m in post_msg:
                    if check_key_msg(m.message, key_words)[0] and m.id not in all_msg:
                        # send message to user with key words and message
                        notify_user(check_key_msg(m.message, key_words)[1], target_group.title, m.id, target_group.id)
                        all_msg.append(m.id)

                all_msg = all_msg[::-1]
        time.sleep(time_pause)

if __name__ == "__main__":
    main()