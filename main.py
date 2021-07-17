#@author Deepak sai pendyala 

import tweepy
import time

auth = tweepy.OAuthHandler('enter your access Api key here','enter your access Api secret key here')
auth.set_access_token('enter your access Token key here', 'enter your access Token secret key here')
api = tweepy.API(auth)

user = api.me()

#print about yourself

print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

#print tweets in your timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(300)
  except StopIteration:
    return

# followback bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  print(follower.name)
  follower.follow()

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
search = "deepak"
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
