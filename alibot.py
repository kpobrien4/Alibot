import tweepy
from keys import *
import sys
import time
from random import random
import os
from os import environ
import json
import requests

# CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
# CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
# ACCESS_KEY = os.environ.get('ACCESS_KEY')
# ACCESS_SECRET = os.environ.get('ACCESS_SECRET')


INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  tweet every 15 seconds

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def hello():
    return("I'm at the grocery store, " + str(random()))


while True:
    print("Tweeting...")
    helloVar = hello()
    api.update_status(helloVar)
    time.sleep(INTERVAL)