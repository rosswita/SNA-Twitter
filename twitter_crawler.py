import tweepy 
from twitter_credential import *

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_toker, access_token_secret)

API = tweepy.API(auth)
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        with open('Data/fetched_tweets_try.json','a') as tf:
            tf.write(data)
        return True

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = API.auth, listener=myStreamListener)

myStream.filter(track=['Euro2020'], is_async=True)

