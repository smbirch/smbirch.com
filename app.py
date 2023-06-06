from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
