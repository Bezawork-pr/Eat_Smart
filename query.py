#!/usr/bin/python3
"""Handles query after creating a new session"""
from engine import DataBase, engine
from sqlalchemy.orm import sessionmaker
from session import session
#Session = sessionmaker(bind=engine)
#session = Session()
#for i in session.query(DataBase).all():
#    print("Are u getting printed".format(i.tweet_id))
print("it is I")

for class_instance in session.query(DataBase).all():
    print(class_instance)
