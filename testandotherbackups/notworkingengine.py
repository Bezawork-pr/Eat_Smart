#!/usr/bin/python3
"""This file connects to the database"""
from flask_sqlalchemy import SQLAlchemy
from app import app 
from flask_login import UserMixin
from datetime import datetime
import os
import mysql.connector

app.config['SQLALCHEMY_DATABASE_URI'] = ("mysql+mysqlconnector://"+ os.environ['ES_MYSQL_USER'] + ":"
                                         + os.environ['ES_MYSQL_PWD']+ "@"
                                         + os.environ['ES_MYSQL_HOST'] + "/"
                                         + os.environ['ES_MYSQL_DB']
                                         + ":3306/innodb")
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

class database(db.Model, UserMixin):
    __tablename__ = 'database'
    tweet_id = db.Column(db.Integer, primary_key=True, nullable=False)
    tweet = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, tweet):
        self.tweet = tweet
