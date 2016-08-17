from dotenv import load_dotenv
import json
import os
import tweepy

load_dotenv('.env')


class TwitterStreamListener(tweepy.StreamListener):

    def on_error(self, status):
        if status == 401:
            print("401 Unauthorized")
        elif status == 420:
            print("Rate limited")
            # Disconnect stream
        else:
            print("Error", status)
        return False

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        print(data)
        return True

auth = tweepy.OAuthHandler(os.environ.get("TWITTER_KEY"), os.environ.get("TWITTER_SECRET"))
auth.set_access_token(os.environ.get("TWITTER_TOKEN"), os.environ.get("TWITTER_TOKEN_SECRET"))

api = tweepy.API(auth)

stream_listener = TwitterStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

locations = os.environ.get('LOCATIONS').split(",")

for i,l in enumerate(locations):
    locations[i] = float(l)

stream.filter(locations=locations, async=True)
