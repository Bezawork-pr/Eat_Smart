#!/usr/bin/python3
"""This file connects to the database using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from os import getenv
import mysql.connector

Base = declarative_base()
ES_MYSQL_USER = 'es_dev'
ES_MYSQL_PWD = 'es_dev_pwd'
ES_MYSQL_HOST = 'localhost'
ES_MYSQL_DB = 'es_dev_db'
engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.
                                      format(ES_MYSQL_USER,
                                             ES_MYSQL_PWD,
                                             ES_MYSQL_HOST,
                                             ES_MYSQL_DB),
    connect_args={'auth_plugin': 'mysql_native_password'})

class EatSmartUser(Base):
    """class EatSmartUser"""
    __tablename__ = 'eatsmartuser'
    id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(80), nullable=False, unique=True)
    email = Column(String(80), nullable=False)
    password =  Column(String(80), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    eatsmarttweet = relationship("EatSmartTweet",
                              backref="eatsmartuser",
                              cascade="all, delete, delete-orphan")
    eatsmartcomment = relationship("EatSmartComment", backref="eatsmartuser", cascade="all, delete, delete-orphan")



    def __init__(self, user_name, email, password):
        """Init function that gets user name email and password through app file, and app file get this contents through the form rendered in template when users are filling out the form"""
        self.user_name = user_name
        self.email = email
        self.password = password


class EatSmartTweet(Base):
    """class EatsmartTweet"""
    __tablename__ = 'eatsmarttweet'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id =  Column(Integer, ForeignKey('eatsmartuser.id'), nullable=False)
    tweet = Column(String(1024), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    eatsmartcomment = relationship("EatSmartComment", backref="eatsmarttweet", cascade="all, delete, delete-orphan")

    def __init__(self, tweet, user_id):
        """This function initates the EatSmartTweet class from the app file using tweet filed by the user on the tweet page.
        And user_id that is found in the eatsmartuser table in the database"""
        self.tweet = tweet
        self.user_id = user_id

class EatSmartComment(Base):
    """class EatSmartComment"""
    __tablename__ = 'eatsmartcomment'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('eatsmartuser.id'), nullable=False)
    tweet_id = Column(Integer, ForeignKey('eatsmarttweet.id'), nullable=False)
    comment = Column(String(1024), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, user_id, tweet_id, comment):
        """This method initiates the EatSmartComment class from the app file using tweet_id and user_id provided by user"""
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.comment = comment


Base.metadata.create_all(engine)
