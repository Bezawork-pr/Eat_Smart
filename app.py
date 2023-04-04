#!/usr/bin/python3
"""This file contains Flask instance that routes the address entered on the site with
what is assigned using render_template"""


from flask import Flask, render_template, url_for, request, redirect
from engine import EatSmartUser, EatSmartTweet, EatSmartComment
from importlib import reload
logged = []
flag = 0
app = Flask(__name__)


@app.route('/')
def index():
  """function index routes the site to the index.html"""
  import session # imports and reloading is necessary to get fresh input from the database
  reload(session)
  from session import usertweet, tweet_list, user_list, comment_list, tweetcomment
  logout = request.args.get('logout')
  if logout == "true": # if user is logged out updatting list logged index 0 to be loggout
      if len(logged) == 0:
          user_logged_out = "loggedout"
          logged.append(user_logged_out)
      elif len(logged) == 1:
          logged[0] = "loggedout"
  else:
      if len(logged) == 0:
        user_logged_out = "loggedout"
        logged.append(user_logged_out) # this is logged out because user is not directed from login page
  return render_template('index.html', logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)


@app.route('/registration', methods =["GET", "POST"])
def registration():
    """This function renders registration page and adds user to database"""
    if request.method == "POST":
        user = request.form['user']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']
        if password != repassword:
            print("password don't match")
            return render_template('registration.html')
        import session
        reload(session)
        from session import user_list, session
        for i in user_list:
            if user == i.user_name or email == i.email: # if username or email has been taken print out username or email not available
                print("Username/email not available")
                return render_template('registration.html')
        create_db = EatSmartUser(user, email, password)
        session.add(create_db)
        session.commit() # user is added and commited to database and directed to login page
        return render_template('login.html')
    return render_template('registration.html')

@app.route('/login', methods =["GET", "POST"])
def login():
    """This function renders login page and checks if username and password
    exists in the database. After that directs user to tweet page where they can add tweets"""
    import session
    reload(session)
    from session import user_list, usertweet, tweetcomment, tweet_list, comment_list
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        for i in user_list:
            if i.user_name == user and i.password == password: # if username and password is found in the database user name is appended to list logged rather than logged out. And the user name will be in the right corner of the site
                if len(logged) == 0:
                  logged.append(user)
                elif len(logged) == 1:
                  logged[0] = user
                flag = 1
                return tweetmytweet()
    logout = request.args.get('logout')
    if logout == "true":
      return index() # if user decides to logout user will directed to the index page where user will not have access to tweet
    return render_template('login.html')

@app.route('/tweet', methods =["GET", "POST"])
def tweetmytweet():
    """This function renders the tweet page where user can tweet.
    This page cannot be accessed directly if user has not logged in"""
    import session
    reload(session)
    from session import session, user_list, usertweet, tweetcomment, tweet_list, comment_list
    if request.method == "POST":
       import session
       reload(session)
       from session import session, user_list, usertweet, tweetcomment, tweet_list, comment_list
       user_id = None
       try: # used try because after loggin when user is directed to this page the method is still post so this handles the error when there is no tweet sent from the form
         tweeted = request.form['my_tweet']
       except Exception as Redirected:
         return render_template("tweet.html", logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
       for i in user_list: # this loop goes through the user's list in the database and get the user id
           if len(logged) == 1:
               if logged[0] != "loggedout":
                 if i.user_name == logged[0]: 
                    user_id = i.id
       if user_id is None: # if the user cannot be found in the database. User will be directed to registration page
           return render_template('registration.html')
       create_db = EatSmartTweet(tweeted, user_id) # when tweet is entered, the tweet will be added and commited 
       session.add(create_db)
       session.commit()
       session.close()
       import session # After reload user can instantly view the tweet just made
       reload(session)
       from session import session, user_list, usertweet, tweetcomment, tweet_list, comment_list
       return render_template("tweet.html", logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
    logout = request.args.get('logout')
    if logout == "true": # When user logs out they will be directed to index page where there is just viewing option to tweets
       return index()
    if len(logged) == 1: # If user is not logged out they can make more tweets
       if logged[0] != "loggedout":
           return render_template("tweet.html", logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
    return redirect(url_for('login')) # If users have no right to make tweets user will be redirected to login page


@app.route('/comment', methods =["GET", "POST"])
def comment():
    """This function adds comment to tweets"""
     if request.method == "POST":
         user_id = request.form['user_id']
         tweet_id = request.form['tweet_id']
         comment = request.form['comment']
         from session import session, tweet_list
         for i in tweet_list:
             if i.user_id == int(user_id) and i.id == int(tweet_id):
                 db_create = EatSmartComment(user_id, tweet_id, comment)
                 session.add(db_create)
                 session.commit()
                 session.close()
                 #return render_template('index.html', usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
                 return index()
     return render_template('comment.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007)
