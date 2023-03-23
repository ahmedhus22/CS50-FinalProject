from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check")
def check():
    inputUrl = request.args.get("url")
    # Regex from https://gist.github.com/dperini/729294
    regex = re.compile(r'^(?:(?:(?:https?|ftp):)?\/\/)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+(?:[a-z\u00a1-\uffff]{2,}\.?))(?::\d{2,5})?(?:[/?#]\S*)?$/i')
    if not regex.search(inputUrl):
        print('regex')
    # TO DO check if the url is possibly safe
    # TO DO update the phishing links table
    
    return render_template("check.html")