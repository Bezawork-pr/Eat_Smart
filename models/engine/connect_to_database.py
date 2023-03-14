#!/usr/bin/python3
"""This file connects to the database"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import random

Base = declarative_base()
engine = create_engine("sqlite:///sqlalchemy.sqlite", echo=True)

class DataBase(Base):
    """class DataBase"""
    __tablename__ = 'database'
    tweet_id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

Base.metadata.create_all(engine)
