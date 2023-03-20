#!/usr/bin/python3
from flask import Flask, render_template, url_for
from session import output_list
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', output_list=output_list)

@app.route('/registration')
def registration():
  return render_template('registration.html')

@app.route('/login')
def login():
  return render_template('login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007)
