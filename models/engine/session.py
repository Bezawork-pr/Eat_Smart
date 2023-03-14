#!/usr/bin/python3
"""This file contains a class that creates a session"""
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from engine import database, engine
from sqlalchemy.orm import sessionmaker
import random
Session = sessionmaker(bind=engine)
session = Session()
my_list = ["dog", "cat","mouse", "chicken"]
for i in range(20):
    word = random.choice(my_list)
    create_db = database(word)
    session.add(create_db)
session.commit()
print("It is me")
for i in session.query(database).all():
    print("it is i {}".format(i))

