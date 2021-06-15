from os import write
import tweepy 
from twitter_credential import *
import json, time

# Process start after 10 sec
# time.sleep(10) 

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_toker, access_token_secret)

API = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, time_limit = 1):
        self.dataset = []
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('tweets_data.json','a')
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        # if ((time.time() - self.start_time) < self.limit):

            # print("ciao")
            record = {
                "created_at": status.created_at
            }

            self.dataset.append(record)
            self.saveFile.write(str(self.dataset))
            # return True
        # else:
            # print(self.dataset)
            # return False

    def on_timeout(self):
        return super().on_timeout()


        # if((time.time() - self.start_time) < self.limit):
        #     print("ciao")
        # data = []
        # if(time.time() - self.start_time) < self.limit:
        #     record = "1233"
        #     # {
        #     #     "created_at": status.created_at
        #     # }
        #     data.append(record)
        #     print(data)
        #     return True
        # else:
        #     print(data)
        #     return False

    def on_error(self, status_code):
        print('Error with status code:')
        print(status_code)
        return False
    
    # def on_status(self, status):
    #       print("sto cazzo!")
        # if(time.time() - self.start_time) < self.limit:
          
        #     record = {
        #         "created_at": status.created_at
        #     }
        #     self.dataset.append(record)
        #     return True
        # else:
        #     print(self.dataset)
        #     return False

    # def on_data(self, data):
    #     if(time.time() - self.start_time) < self.limit:
    #         record = {
    #             "created_at": status.crated_at
    #         }
    #         self.datase
    #         return True
    #     else:
    #         self.saveFile.close()
    #         return False

        # tweet = json.loads(data)
        # d = {}
        # d['created_at'] = tweet['created_at']
        # dataset.append(d)
        # with open('tweets_data.json','a') as tf:
        #     tf.write(str(dataset))
        # return True
    

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = API.auth, listener=myStreamListener)

myStream.filter(track=['Euro2020'], is_async=True)