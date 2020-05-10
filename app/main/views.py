from . import main
from flask import render_template, request, redirect

@main.route("/")
def index():

    title="Pitch"
    return render_template("index.html", title=title)