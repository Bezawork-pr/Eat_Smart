#!/usr/bin/python3
from flask import Flask, render_template, url_for, request, redirect
from engine import EatSmartUser, EatSmartTweet, EatSmartComment
from importlib import reload
logged = []
flag = 0
app = Flask(__name__)


@app.route('/')
def index():
  import session
  reload(session)
  from session import usertweet, tweet_list, user_list, comment_list, tweetcomment
  logout = request.args.get('logout')
  print(logout)
  if logout == "true":
      if len(logged) == 0:
          user_logged_out = "loggedout"
          logged.append(user_logged_out)
      elif len(logged) == 1:
          logged[0] = "loggedout"
  else:
      if len(logged) == 0:
        user_logged_out = "loggedout"
        logged.append(user_logged_out)
  return render_template('index.html', logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)


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
        import session
        reload(session)
        from session import user_list, session
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
    import session
    reload(session)
    from session import user_list, usertweet, tweetcomment, tweet_list, comment_list
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        for i in user_list:
            if i.user_name == user and i.password == password:
                if len(logged) == 0:
                  logged.append(user)
                elif len(logged) == 1:
                  logged[0] = user
                flag = 1
                return tweetmytweet()
    logout = request.args.get('logout')
    if logout == "true":
      return index()
    return render_template('login.html')

@app.route('/tweet', methods =["GET", "POST"])
def tweetmytweet():
    import session
    reload(session)
    from session import session, user_list, usertweet, tweetcomment, tweet_list, comment_list
    if request.method == "POST":
       import session
       reload(session)
       from session import session, user_list, usertweet, tweetcomment, tweet_list, comment_list
       user_id = None
       try:
         tweeted = request.form['my_tweet']
       except Exception as Redirected:
         return render_template("tweet.html", logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
       for i in user_list:
           if len(logged) == 1:
               if logged[0] != "loggedout":
                 if i.user_name == logged[0]:
                    user_id = i.id
       if user_id is None:
           return render_template('registration.html')
       create_db = EatSmartTweet(tweeted, user_id)
       session.add(create_db)
       session.commit()
       session.close()
       import session
       reload(session)
       from session import session, user_list, usertweet, tweetcomment, tweet_list, comment_list
       return render_template("tweet.html", logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
    logout = request.args.get('logout')
    if logout == "true":
       return index()
    if len(logged) == 1:
       if logged[0] != "loggedout":
           return render_template("tweet.html", logged=logged[0], usertweet=usertweet, tweetcomment=tweetcomment, tweet_list=tweet_list, user_list=user_list, comment_list=comment_list)
    return redirect(url_for('login'))


@app.route('/comment', methods =["GET", "POST"])
def comment():
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
