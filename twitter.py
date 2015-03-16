from tweepy import OAuthHandler, API
# from header import consumer_key, consumer_secret, access_token, access_token_secret
from dateutil import parser
import os


consumer_key = os.environ.get('consumer_key', None)
consumer_secret = os.environ.get('consumer_secret', None)
access_token = os.environ.get('access_token', None)
access_token_secret = os.environ.get('access_token_secret', None)


def get_tweets():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)

    tweets = api.user_timeline(screen_name='TrustyJohn', count=5)

    pay_load = []
    for tweet in tweets[:5]:
        tweet_json = {}
        tweet_json['text'] = tweet._json['text']
        date = tweet._json['created_at']
        tweet_json['date'] = parser.parse(date)
        pay_load.append(tweet_json)

    return pay_load
