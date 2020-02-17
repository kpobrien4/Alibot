import tweepy
from keys import *
import sys
import time
from random import random
import os
from os import environ
import json
import requests
import random
from alibi import *

# CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
# CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
# ACCESS_KEY = os.environ.get('ACCESS_KEY')
# ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

resp = requests.get(api_url)
for data in resp.json():
    crime_description = data["pd_desc"]

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  tweet every 15 seconds

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def alibi():
    return(random.choice(alibis) + ", NOT committing " + crime_description.lower())


while True:
    print("Crafting the perfect alibi...")
    alibiVar = alibi()
    api.update_status(alibiVar)
    time.sleep(INTERVAL)