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
