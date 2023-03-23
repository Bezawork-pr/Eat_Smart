#!/usr/bin/python3
from flask import Flask, render_template, url_for, request
from engine import EatSmartUser, EatSmartTweet, EatSmartComment
from session import session, usertweet, tweetcomment, tweet_list, user_list, comment_list
app = Flask(__name__)

def query():
    #from session import output_list
    #output_list = []
    #for i in session.query(EatSmart).all():
    #   new_instance = retrive(i.tweet_id, i.user, i.tweet, i.email, i.created_at, i.updated_at)
    #    output_list.append(new_instance)
    return output_list

@app.route('/')
def index():
  #output_list = query()
  return render_template('index.html', output_list=tweet_list)

@app.route('/registration')
def registration():
  return render_template('registration.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/tweet', methods =["GET", "POST"])
def tweetmytweet():
    if request.method == "POST":
       tweeted = request.form['my_tweet']
       user = request.form['user']
       email = request.form['email']
       create_db = EatSmart(tweeted, user, email)
       session.add(create_db)
       session.commit()
       #output_list = query()
       return render_template('index.html', output_list=tweet_list)
    return render_template("tweet.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007)
