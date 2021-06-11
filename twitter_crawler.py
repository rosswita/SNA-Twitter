import tweepy 
from twitter_credential import *

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_toker, access_token_secret)

API = tweepy.API(auth)

public_tweet = tweepy.Cursor(API.search, q="euro2021", result_type="popular", tweet_mode="extended").items(20)
    

for tweet in public_tweet:
    tweet_text = tweet.full_text
    print(tweet_text)