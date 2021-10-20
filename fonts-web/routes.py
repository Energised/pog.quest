"""
IndexController.py
@author Dan Woolsey
Basic webpage for testing Flask and integrating fonts\ library

TO EXECUTE
  export FLASK_APP=IndexController   -
  $env:FLASK_APP = "hello"           - POWERSHELL
  flask run
FOR DEVELOPMENT MODE
  export FLASK_ENV = development - BASH
  $env:FLASK_ENV = "development" - POWERSHELL
  flask run
"""

from flask import Flask, render_template

from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                            title="Henry Winklers Headlines",
                            description="Sit on it!")

@app.route("/about")
def about():
    return "<h1> About </h1>"

@app.route("/<example>")
def test_parameters(example):
    return f"Hello, {escape(example)}!"
