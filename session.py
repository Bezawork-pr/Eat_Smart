#!/usr/bin/python3
"""This file contains a class that creates a session"""
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from engine import EatSmart, engine
from sqlalchemy.orm import sessionmaker
import random
from random_username.generate import generate_username
Session = sessionmaker(bind=engine)
session = Session()
tweets = ["dog", "cat","mouse", "chicken"]
users = generate_username(20)
output_list =  []
for i in range(20):
    tweeted = random.choice(tweets)
    user = random.choice(users)
    email = user + '@gmail'
    create_db = EatSmart(tweeted, user, email)
    session.add(create_db)
session.commit()
class retrive:
    def __init__(self, tweet_id, user, tweet, email, created_at, updated_at):
        self.id = tweet_id
        self.user = user
        self.tweet = tweet
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

for i in session.query(EatSmart).all():
    new_instance = retrive(i.tweet_id, i.user, i.tweet, i.email, i.created_at, i.updated_at)
    output_list.append(new_instance)
