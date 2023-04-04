#!/usr/bin/python3
"""This file contains a class that creates a session based on the engine created
in the file engine"""
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from engine import EatSmartUser, EatSmartTweet, EatSmartComment, engine
from sqlalchemy.orm import sessionmaker
import random
from random_username.generate import generate_username
Session = sessionmaker(bind=engine)
session = Session() 
tweet_list =  [] # retrived tweet list from the database will be stored here
comment_list = [] # retrived comment_list from the database will be stored here
user_list = [] # retrived user list from the database will be stored here

class RetriveUsers:
    """class RetriveUsers"""
    def __init__(self, id, user_name, email, password, created_at):
        """This method initiates the class RetriveUsers"""
        self.id = id
        self.user_name= user_name
        self.email = email
        self.password = password
        self.created_at = created_at

class RetriveTweets:
    """class RetriveTweets"""
    def __init__(self, id, user_id, tweet, created_at):
        """This method initiates the class RetriveTweets"""
        self.id = id
        self.user_id = user_id
        self.tweet = tweet
        self.created_at = created_at


class RetriveComments:
    """class RetriveComments"""
    def __init__(self, id, user_id, tweet_id, comment, created_at):
        """This method initiates the class RetriveComments"""
        self.id = id
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.comment = comment
        self.created_at = created_at


for i in session.query(EatSmartUser).all():
    """Here session.query(class).all() gets all the users created. And the for loop goes through
    each content and stores the content using a class RetriveUsers which is then appended to class users_list"""
    user_retrived = RetriveUsers(i.id, i.user_name, i.email, i.password, i.created_at)
    user_list.append(user_retrived)
user_list.reverse()

for i in session.query(EatSmartTweet).all():
    """Here session.query(class).all() gets all the tweets created. And the for loop goes through
    each content and stores the content using a class RetriveTweets which is then appended to class tweet_list"""
    retrived_tweet = RetriveTweets(i.id, i.user_id, i.tweet, i.created_at)
    tweet_list.append(retrived_tweet)
tweet_list.reverse()

for i in session.query(EatSmartComment).all():
    """Here session.query(class).all() gets all the comments created. And the for loop goes through
    each content and stores the content using a class RetriveComments which is then appended to class comment_list"""
    retrived_comment = RetriveComments(i.id, i.user_id, i.tweet_id, i.comment, i.created_at)
    comment_list.append(retrived_comment)
comment_list.reverse()

def usertweet(user_id):
    """This function is not implemented yet. I wanted to show all the tweets made by a specific person in one page"""
    for tweet in tweet_list:
        if tweet.user_id == user_id:
            tweet_by_user =  []
            tweet_by_user.append(tweet)
    tweet_by_user.reverse()
    return tweet_by_user

def tweetcomment(tweet_id):
    """This function matches tweets with comments to them"""
    for comment in comment_list:
        if comment.tweet_id == tweet_id:
            comment_on_tweet = []
            comment_on_tweet.append(comment)
    comment_on_tweet.reverse()
    return comment_on_tweet
