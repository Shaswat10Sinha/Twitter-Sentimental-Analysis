# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 01:14:32 2022

@author: Shaswat Sinha
"""

# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer


# Authentication
bearerToken=""
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""


client = tweepy.Client(bearer_token=bearerToken,consumer_key= consumerKey,
                       consumer_secret= consumerSecret,access_token= accessToken,
                       access_token_secret= accessTokenSecret,return_type = dict)


#Sentiment Analysis
def percentage(part,whole):
 return 100 * float(part)/float(whole)

keyword = "world cup"
noOfTweet = 2500
tweets = client.search_recent_tweets(query=keyword, max_results=100)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet1 in tweets.values():    
    print(tweet1)

for tweet2 in tweets.values():
    x=tweets['data']

print(x)


#All the tweets for the last 
tweets=[d['text'] for d in x]


nltk.download('vader_lexicon')

for tweet in tweets:
    
    #print(tweet.text)
    #tweet_list.append(x.text)
    analysis = TextBlob(tweet)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity
    
    if neg > pos:
        negative_list.append(tweet)
        negative += 1

    elif pos > neg:
        positive_list.append(tweet)
        positive += 1
    
    elif pos == neg:
        neutral_list.append(tweet)
        neutral += 1

positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

#creating pie chart
labels = ['Positive' , 'Neutral','Negative']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword=  "+keyword+"" )
plt.axis('equal')
plt.show()

