#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import argparse
import tweepy
import textblob.exceptions
from textblob import TextBlob


# Twitter API credentials
consumer_key = "Moc9bluqyuBYKXE8z7tN1WxmX"
consumer_secret = "laqaAU8CqhEXuI6BnmMNCjzWJUAbc4pzxDB3pQQAj6WwqrRVFh"
access_key = "44663631-9o53tPhZTg2Oeip2o53K7m6k3PehTLb69MN7WowQv"
access_secret = "n1rf4VeYDL2rZUaMXtxniYAGOB314QqiPP3NeoHz6JTOW"

# Command line
parser = argparse.ArgumentParser(prog="tweets-acquisition", description="Get user's tweets")

# Argument
parser.add_argument("--user", type=str, help="Twitter's username", required=True)

# Parse command line
args = parser.parse_args()

# Authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Get API
api = tweepy.API(auth)

# Get user
user = api.get_user(args.user)

# Get statuses
for status in api.user_timeline(screen_name=args.user, count=200):
    # Analyse tweet
    tweet = TextBlob(status.text)

    # Show sentiment analysis
    print(u"Tweet \"{}\"".format(status.text))
    print(u"Polarity {}, Subjectivity {}".format(tweet.sentiment.polarity, tweet.sentiment.subjectivity))
    print(u"Language : {}".format(tweet.detect_language()))
    try:
        print(u"French : {}".format(tweet.translate(from_lang="en-US", to='fr')))
    except textblob.exceptions.NotTranslated:
        pass
    # end try
    print(u"Tokens : {}".format(tweet.words))
    print(u"")
# end for
