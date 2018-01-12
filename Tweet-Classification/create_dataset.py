#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import tweepy
import pickle
import codecs

# Republican users
users = dict()
users['republicans'] = ["realDonaldTrump", "marcorubio", "JeffFlake", "RandPaul", "lisamurkowski", "SenToomey",
                        "SenJohnMcCain", "tedcruz", "ChuckGrassley", "SenatorCollins", "SenDeanHeller", "JerryMoran",
                        "SenatorTimScott", "SenTomCotton", "senrobportman"]
users['democrats'] = ["HillaryClinton", "BillClinton", "BarackObama", "SenBobCasey", "SenGillibrand", "SenBillNelson",
                      "SenFeinstein", "SenSchumer", "SenBlumenthal‏", "SenJeffMerkley‏", "SenatorHeitkamp", "SenSanders",
                      "SenatorTomUdall", "SenBennetCO", "SenWhitehouse"]


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
for c in users.keys():
    for user in users[c]:
        # Get statuses
        for status in api.user_timeline(screen_name=user, count=200):
            X.append(status.text)
            Y.append(c)
        # end for
    # end for
# end for

pickle.dump((X, Y), codecs.open(u"dataset.p", 'wb'))
