from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #For app2 change the following message to: "Welcome to app2"
    return "Welcome to app1!"

@app.route('/hello', methods=['GET'])
def mypage():
    return "Hello World!"