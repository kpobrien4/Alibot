import tweepy
import sys
import time
import json
import requests
import random

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
api_url = environ['api_url']

alibis = ["At the grocery store", "Watching a movie with Howie Mandell", "Reading about current events", "At a Chicago White Socks game", "Narrating an audio book", "Partying at the White House", "Observing a UFO"]

resp = requests.get(api_url)
desc = resp.json()[0]["pd_desc"]

#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 15  # tweet every 15 seconds

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