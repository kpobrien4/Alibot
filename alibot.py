import tweepy
from keys import *
import sys
import time
from random import random
import os
from os import environ

# CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
# CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
# ACCESS_KEY = os.environ.get('ACCESS_KEY')
# ACCESS_SECRET = os.environ.get('ACCESS_SECRET')



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def hello():
    return("Hello " + str(random()))


while True:
    print("Tweeting...")
    helloVar = hello()
    api.update_status(helloVar)
    time.sleep(INTERVAL)