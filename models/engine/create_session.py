#!/usr/bin/python3
"""This file contains a class that creates a session"""
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from connect_to_database import DataBase, engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
for i in range(20):
    create_db = DataBase()
    session.add(create_db)
session.commit()

