import tweepy 
from twitter_credential import *

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_toker, access_token_secret)



class listener(tweepy.StreamListener):

    def on_status(self, status):
        userid = status.user.id_str
        text = status.text
        print(userid + ', ' +text)

    def on_error(self, status_code):
        print('Error with status code:')
        print(status_code)
        return False


auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_toker, access_token_secret)

twitterStream = tweepy.Stream(auth, listener())

# filtro per parola chiave
# twitterStream.filter(track=['euro2020'])

#filtro per location 
twitterStream.filter(locations=[12.30,41.79,12.74,41.96])

# NON si può filtrare contemporaneamente per location e parola chiave

#esempio di twitter per nyc che funziona
#twitterStream.filter(locations=[-74,40,-73,41])


# area urbana Roma
# 41.79,12.74
# 41.96,12.30

# Italia.
# 35.56,12.27
# 47.02,12.19
# twitterStream.filter(locations=[12.19,35.56,12.27,47.02])
