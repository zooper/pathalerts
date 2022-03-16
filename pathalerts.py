import twitter
import telegram
import time
import os

api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
                 consumer_secret=os.environ['CONSUMER_SECRET'],
                 access_token_key=os.environ['ACCESS_TOKEN_KEY'],
                 access_token_secret=os.environ['ACCESS_TOKEN_SECRET'],
                 tweet_mode='extended',)


token = os.environ['TOKEN']
chat_id = os.environ['CHAT_ID']
# Telegram bot settings
bot = telegram.Bot(token=token)
chat_id = chat_id




# Todo
# if Delays, Delayed etc - Add warning icon to telegram message
# if Resumed, resuming etc, - Add green light icon to telegram message

def check_tweets():
    search = api.GetUserTimeline(screen_name="PATHAlerts", count=20)
    for tweet in search:
        if not str(tweet.id) in open("/log/log.txt").read():
            if not "elevator" in str(tweet.full_text):
                log = open("/log/log.txt", "a")
                log.write(str(tweet.id) + "\n")
                msg = tweet.full_text
                try:
                    bot.send_message(
                            chat_id=chat_id,
                            text = msg,
                            parse_mode=telegram.ParseMode.HTML
                            )
                except Exception as e:
                    print("Error connecting to Telegram " + str(e))
            
            print(msg)
while True:
    check_tweets()
    time.sleep(300)




