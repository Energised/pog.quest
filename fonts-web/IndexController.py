# IndexController.py
# @author Dan Woolsey
#
# Basic webpage for testing Flask and integrating fonts\ library


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Welcome! </p>"
