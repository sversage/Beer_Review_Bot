import tweepy, json, time
import markov_twitter_gen
from Twitter_APIs import *


CONSUMER_KEY = api_dict["CONSUMERKEY"]
CONSUMER_SECRET = api_dict['SECRETCONSUMERKEY']
ACCESS_TOKEN = api_dict['ACCESSTOKEN']
ACCESS_SECRET = api_dict['SECRETACCESSTOKEN']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    how_drunk = time.localtime()
    if how_drunk.tm_hour < 10:
        drunk_meter = 4
    elif how_drunk.tm_hour < 13:
        drunk_meter = 3
    elif how_drunk.tm_hour < 17:
        drunk_meter = 2
    else:
        drunk_meter = 1
    try:
        api.update_status(markov_twitter_gen.main('/Users/marcversage/Desktop/Apps/Beer_Review_Bot/data/beer_reviews.txt', drunk_meter))
    except:
        api.update_status(markov_twitter_gen.main('/Users/marcversage/Desktop/Apps/Beer_Review_Bot/data/beer_reviews.txt', drunk_meter))
    time.sleep(3600) # Sleep for one hour
