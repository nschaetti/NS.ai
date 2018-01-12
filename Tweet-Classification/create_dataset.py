#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import tweepy
import pickle
import codecs
import time

# Republican users
users = dict()
users['democrats'] = [u"HillaryClinton", u"BillClinton", u"BarackObama", u"SenBobCasey", u"SenGillibrand", u"SenBillNelson",
                      u"SenFeinstein", u"SenSchumer", u"SenMarkey", u"SenatorHeitkamp", u"SenSanders",
                      u"SenatorTomUdall", u"SenBennetCO", u"SenWhitehouse", u"SenWarren"]
users['republicans'] = [u"realDonaldTrump", u"marcorubio", u"JeffFlake", u"RandPaul", u"lisamurkowski", u"SenToomey",
                        u"SenJohnMcCain", u"tedcruz", u"ChuckGrassley", u"SenatorCollins", u"SenDeanHeller", u"JerryMoran",
                        u"SenatorTimScott", u"SenTomCotton", u"senrobportman"]


# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Get API
api = tweepy.API(auth)

# Data set
X = list()
Y = list()

# For republicans and democrats
for c in ["democrats", "republicans"]:
    print(u"Downloading tweets for class \"{}\"".format(c))
    tweet_text = u""
    for user in users[c]:
        print(u"Downloading tweets for user \"{}\"".format(user))
        # Get statuses
        for status in api.user_timeline(screen_name=user, count=200):
            tweet_text += status.text
        # end for
        X.append(tweet_text)
        Y.append(c)
        time.sleep(60)
    # end for
# end for

pickle.dump((X, Y), codecs.open(u"dataset.p", 'wb', encoding='utf-8'))
