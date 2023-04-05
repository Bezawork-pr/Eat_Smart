# <pre> Eat Smart   ![icons8-project-64](https://user-images.githubusercontent.com/107026397/230062358-fc53818c-1633-44ef-9ba8-9aba5c84609c.png)
</pre>
<p>I am Bezawork Belachew Lindlof:grinning: Student at ALX.</p>

<p>I am inspired to develop this app because it will allow users to make healthier meal choices. With this information, users will be able to identify which meals are the most nutritionally efficient and cost-effective, helping them to reach their dietary goals with confidence.

I am also passionate about helping to reduce the environmental impacts of unsustainable food practices, as this app will allow users to make more informed food choices.

I am driven by the idea that everyone should have access to the tools to properly manage their energy levels, as this could have a profound impact on why some people can be successful and reach their goals, while others are deprived of opportunities due to a lack of awareness. 

For these reasons, I am driven to develop this app. On a larger scale, I hope to help others have better access to understanding their food requirements and making educated decisions when it comes to their meal plans.

But on a personal level, I am highly inspired to make this knowledge accessible to better my own life and performance.

What comes next for this app will be decided on how people find it useful on the beta test.

This app is a Twitter-like app. Users can register on the register page. From the registration form,  their name, email, and password will be saved in the database. Then they will be able to log in. They will be redirected to the registration page if they do not provide the proper username and password they used during registration. After login, users can tweet. Before login, users can't access the tweet page and can only access the index page with tweets but no option to tweet. After tweeting, users can log out and they will be redirected to the index page. Users can comment on other people's tweets.

This is the first self-directed project that we were given by ALX. The struggle I had was figuring out where to start at the beginning of the project. I started building the classes and connecting with the database using SqlAlchemy. After that, I started working with Flask to render HTML pages, which I later modified using Jinja. My working environment was vim on the server where the project is deployed. Making the necessary update and installation had some hickups :upside_down_face:, which took roughly one week of the project week.

Another more technical issue I was having was when users were redirected from the login page to the tweet page. I was getting an error when I called the tweetmytweet function from login, so I decided to render the tweet page separately on the login function and also on the tweetmytweet function. Therefore, the tweet HTML was getting rendered via two routes. Later, after debugging, I found that the reason I was having the error was because when calling the tweetmytweet function from login, it was using the POST method rather than the GET method, so I used a try and except to check if the POST is called with no POST, meaning the tweet form is not filled out. So the code does not break when the user is redirected from the login page to tweet.

```Python 


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

```


##  Site currently deployed at 
[Eat Smart](http://52.6.195.254/)

## Languages used 
[![My Skills](https://skillicons.dev/icons?i=python,html,css,flask)](https://skillicons.dev)

##  Features 
### <pre> Index page </pre>
<img width="800" alt="Screen Shot 2023-03-30 at 16 23 20" src="https://user-images.githubusercontent.com/107026397/230048160-7fcc63d7-fe91-430c-aa90-1216df844e91.png">



### <pre> Registration Page </pre>
<img width="800" alt="Screen Shot 2023-03-30 at 16 26 24" src="https://user-images.githubusercontent.com/107026397/230048216-f9fa8551-9cc6-42b7-88bd-60ae932c4528.png">



### <pre> Login Page </pre>
<img width="800" alt="Screen Shot 2023-03-30 at 16 27 20" src="https://user-images.githubusercontent.com/107026397/230048268-6723de77-159c-45da-b370-dd89dbd0de24.png">



### <pre> Tweet Page </pre>
<img width="800" alt="Screen Shot 2023-04-03 at 15 48 52" src="https://user-images.githubusercontent.com/107026397/230048351-ab45bfa6-f914-4c96-a41f-cf8fc4d6bfa5.png">

### <pre> Comments </pre>
<img width="800" alt="Screen Shot 2023-03-30 at 16 29 14" src="https://user-images.githubusercontent.com/107026397/230049605-ee84a474-f585-4552-9080-a8396f8b5867.png">


## Installation

Install Eat_Smart by download

```bash
  git clone https://github.com/Bezawork-pr/Eat_Smart
  cd Eat_Smart
```

## Usage/Examples

```Python (Add more features in app)

@app.route('/profile', methods =["GET", "POST"])
def profile(): 
  return render_template('profile.html')

```
## Contributing

Contributions are always welcome!


## Related

Here are some related projects

[AirBnB_clone_v4](https://github.com/Bezawork-pr/AirBnB_clone_v4)

## Author

- [@bezawork Lindlof Github](https://www.github.com/bezawork-pr/)
- [@bezawork Lindlof Linkedin](https://www.linkedin.com/in/bezaworklindlof/)
- [@bezawork Lindlof Medium](https://medium.com/@bezaworkalx)
## Acknowledgements

 [ALX](https://www.alxafrica.com/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
