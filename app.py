from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check")
def check():
    '''Checks if the entered url is suspicious or not'''
    inputUrl = request.args.get("url")

    # Regex for verify if the url entered is valid or not group(2) contains the 2nd level domain
    # For complete reference on valid urls refer: https://datatracker.ietf.org/doc/html/draft-liman-tld-names-06 and https://stackoverflow.com/questions/7930751/regexp-for-subdomain
    regex = re.compile(r'''(
        (?:https?://)?              # http or https is optional
        (?:[A-Za-z0-9\-_]{0,63}     # matches the sub domain and is optional
        \.
        )?
        ([A-Za-z0-9\-_]{1,63})      # matches the 2nd level domain and will be stored in match object group 2 if found
        \.
        (?:[A-Za-z]{1,63})
    )''',re.VERBOSE)

    # TO DO check if the url is possibly safe
    # TO DO update the phishing links table
    
    return render_template("check.html")