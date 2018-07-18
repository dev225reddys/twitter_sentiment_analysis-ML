import tweepy
from textblob import TextBlob

consumer_key= 'dluUBUYk266ncbacMMIdUwnnt'
consumer_secret = 'BvxfNap4haU6LIxpCL0rlXBG7SVuwjrA3HmEITeqL6vz17wzNk'
access_token = '466207152-a0aZpYJr4LQrhOi4U3YEbe3u51t3Cy4VE87H4mjD'
access_token_secret = 'OlpQV1sZm3ulNbHXcqso1zV1ko5gFniUDk8CXpGw8kXQI'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)