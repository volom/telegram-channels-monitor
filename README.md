TELEGRAM CHANNELS MONITOR helps monitor channels for messages with certain keywords (Monitoring telegram channels messages by keywords and forwarding them to your telegram bot).

If you don't have enough time to scroll through all channels, but you are interested in posts with certain words, you just need to use this tool by following some steps:

1. Save the folder with the project and open it

2. Install all needed libraries:
```
pip3 install -r requirements.txt
```
3. Put your credentials in *auth_info.py*:
    from https://my.telegram.org/ set values into variables:
        *session_name*
        *api_id*
        *api_hash*
    create telegram bot in telegram BotFather (https://t.me/BotFather) and put your bot token into *bot_token*
    (!) The bot has to be launched

4. Edit *run_monitoring.py*. Define target channels in the 'monitoring_channels' by setting their names and inserting the keywords in the 'key_words' variable. You can also set the frequency of updating requests to channels in the "time_pause" variable and define a limit on the number of simultaneously checked messages in "limit_msg"

5. Run *run_monitoring.py*
```
python3 run_monitoring.py
```
