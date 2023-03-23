from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index</p>"