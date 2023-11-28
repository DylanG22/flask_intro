
from flask import Flask, request 

app = Flask(__name__)

@app.route('/welcome')
def wel():
    return 'welcome'

@app.route('/welcome/home')
def wel_home():
    return 'welcome home'

@app.route('/welcome/back')
def wel_back():
    return 'welcome back'