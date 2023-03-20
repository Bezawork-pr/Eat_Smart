#!/usr/bin/python3
"""This file connects to the database"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
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

class EatSmart(Base):
    """class EatSmart"""
    __tablename__ = 'eatsmart'
    tweet_id = Column(Integer, primary_key=True, nullable=False)
    user = Column(String(80), nullable=False)
    tweet = Column(String(1024), nullable=False)
    email = Column(String(80), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, tweet, user, email):
        self.tweet = tweet
        self.user = user
        self.email = email

Base.metadata.create_all(engine)
