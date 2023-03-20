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

class database(Base):
    """class DataBase"""
    __tablename__ = 'database'
    tweet_id = Column(Integer, primary_key=True, nullable=False)
    tweet = Column(String(1024), nullable=False) 
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, tweet):
        self.tweet = tweet

Base.metadata.create_all(engine)
