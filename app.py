from flask import Flask, request, redirect, render_template
import re
import database, scrape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check")
def check():
    """Checks if the entered url is suspicious or not"""
    url = request.args.get("url")

    # Regex to verify if the url entered is valid or not group(2) contains the 2nd level domain
    # For complete reference on valid urls refer: https://datatracker.ietf.org/doc/html/draft-liman-tld-names-06 and https://stackoverflow.com/questions/7930751/regexp-for-subdomain
    regex = re.compile(r'''(
        (?:https?://)?              # http or https is optional
        (?:[A-Za-z0-9\-_]{0,63}     # matches the sub domain
        \.
        )
        ([A-Za-z0-9\-_]{1,63})      # matches the 2nd level domain and will be stored in match object group 2 if found
        \.
        (?:[A-Za-z]{1,63})
    )''',re.VERBOSE)

    match = regex.search(url)

    # Check if the url is possibly safe
    # if no matches match object will contain None
    if not match is None:
        name = match.group(2)
        properurl = scrape.formaturl(url)
        # Check if the url exists in the database
        if database.isurlFake(match.group()):
            return render_template("fake.html", url=properurl)
        # Check if the url is possibly suspicious by browing the web
        if scrape.verify(url):
            return render_template("safe.html", url=properurl)
        else:
            # If the url is not safe add it to the database
            database.inserturl(properurl, name)
            return render_template("fake.html", url=properurl)
    else:
        return redirect("/")