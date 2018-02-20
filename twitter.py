import tweepy
from tweepy import OAuthHandler
import unicodedata
import collections

def twitter_connection():
    consumer_key = 'NajUq95poVcCoDp4TJtgj0lVd'
    consumer_secret = 'dZUbYGHvtJ3r2m8JRqh7YmTOvzJcodjtzWYPSmI7Tt00O3Skg8'
    access_token = '964180915202199552-Wk5VNneAAWRVMpJkyYM5qUX1Ljo6Afv'
    access_secret = 'Qp2Ina1kyVyHwDAJwNvW7T3YYsuzvQToCBnCMZNfOy9AH'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

username= input('Username/Screen Name:\n')
api=twitter_connection()
tweets= api.user_timeline(id=username, count=10)
L=[]
p = list([',' ,'|' , '.' , ':' , '!' ,' ' ,'#' ,'@' ,'$' ,'%' ,'*' , '"' , '?' , '(' , ')' , "'"])

print('Your ten latest tweets are:\n')
for tweet in tweets:
    L.append(tweet.text)
    if p in L:
        L.remove(p)
    print(tweet.text)


for tweet.text in L:
    for word in tweet.text.split(' '):
        counter=collections.Counter(tweet.text)
        popword=str(counter.most_common(1))

print("Your most popular word is " + popword )
