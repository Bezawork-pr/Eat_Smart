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

  return render_template('index.html', usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)

@app.route('/registration', methods =["GET", "POST"])
def registration():
    if request.method == "POST":
        user = request.form['user']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        if password != repassword:
            print("password don't match")
            return render_template('registration.html')
        for i in user_list:
            if user == i.user_name or email == i.email:
                print("Username/email not available")
                return render_template('registration.html')
        create_db = EatSmartUser(user, email, password)
        session.add(create_db)
        session.commit()
        return render_template('login.html')
    return render_template('registration.html')

@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        for i in user_list:
            if i.user_name == user and i.password == password:
                return render_template('index.html', output_list=tweet_list)
    return render_template('login.html')

@app.route('/tweet', methods =["GET", "POST"])
def tweetmytweet():
    if request.method == "POST":
       user_id = None
       tweeted = request.form['my_tweet']
       user = request.form['user']
       email = request.form['email']
       for i in user_list:
           if i.user_name == user and i.email == email:
               user_id = i.id
       if user_id is None:
           return render_template('registration.html')
       create_db = EatSmartTweet(tweeted, user_id)
       session.add(create_db)
       session.commit()
       return render_template('index.html', usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
    return render_template("tweet.html")

@app.route('/comment', methods =["GET", "POST"])
def comment():
     if request.method == "POST":
         user_id = request.form['user_id']
         tweet_id = request.form['tweet_id']
         comment = request.form['comment']
         for i in tweet_list:
             if i.user_id == int(user_id) and i.id == int(tweet_id):
                 db_create = EatSmartComment(user_id, tweet_id, comment)
                 session.add(db_create)
                 session.commit()
                 return render_template('index.html', usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
     return render_template('comment.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007)
