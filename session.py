#!/usr/bin/python3
"""This file contains a class that creates a session"""
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from engine import EatSmartUser, EatSmartTweet, EatSmartComment, engine
from sqlalchemy.orm import sessionmaker
import random
from random_username.generate import generate_username
Session = sessionmaker(bind=engine)
session = Session()
tweet_list =  []
comment_list = []
user_list = []

class RetriveUsers:
    def __init__(self, id, user_name, email, password, created_at):
        self.id = id
        self.user_name= user_name
        self.email = email
        self.password = password
        self.created_at = created_at

class RetriveTweets:
    def __init__(self, id, user_id, tweet, created_at):
        self.id = id
        self.user_id = user_id
        self.tweet = tweet
        self.created_at = created_at


class RetriveComments:
    def __init__(self, id, user_id, tweet_id, comment, created_at):
        self.id = id
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.comment = comment
        self.created_at = created_at


for i in session.query(EatSmartUser).all():
    user_retrived = RetriveUsers(i.id, i.user_name, i.email, i.password, i.created_at)
    user_list.append(user_retrived)
    user_list.reverse()

for i in session.query(EatSmartTweet).all():
    retrived_tweet = RetriveTweets(i.id, i.user_id, i.tweet, i.created_at)
    tweet_list.append(retrived_tweet)
    tweet_list.reverse()

for i in session.query(EatSmartComment).all():
    retrived_comment = RetriveComments(i.id, i.user_id, i.tweet_id, i.comment, i.created_at)
    comment_list.append(retrived_comment)
    comment_list.reverse()

def usertweet(user_id):
    for tweet in tweet_list:
        if tweet.user_id == user_id:
            tweet_by_user =  []
            tweet_by_user.append(tweet)
    tweet_by_user.reverse()
    return tweet_by_user

def tweetcomment(tweet_id):
    for comment in comment_list:
        if comment.tweet_id == tweet_id:
            comment_on_tweet = []
            comment_on_tweet.append(comment)
    comment_on_tweet.reverse()
    return comment_on_tweet
