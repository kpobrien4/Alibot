import tweepy
from keys import *
import sys
import time
import json
import requests
import random
from alibi import *


resp = requests.get(api_url)
desc = random.choice(resp.json())["pd_desc"]
for data in resp.json():
    crime_description = data["pd_desc"]

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  tweet every 15 seconds

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def alibi():
    return(random.choice(alibis) + ", NOT committing " + desc.lower())


while True:
    print("Crafting the perfect alibi...")
    alibiVar = alibi()
    api.update_status(alibiVar)
    time.sleep(INTERVAL)