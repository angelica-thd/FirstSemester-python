import tweepy
from tweepy import OAuthHandler
import unicodedata
import collections

def twitter_connection():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

username= input('Username/Screen Name:\n')
api=twitter_connection()
tweets= api.user_timeline(id=username, count=10)
L=[]
print('Your ten latest tweets are:\n')
for tweet in tweets:
    L.append((tweet.text).split(' '))
    for word in L:
        counter= collections.Counter(word)
        popword=str(counter.most_common(1))
    print(tweet.text)
print('Your most popular word is ' + popword )
