from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
from ..models import Users

@main.route("/")
def index():

    title="Pitch"
    return render_template("index.html", title=title)

@main.route("/user/<uname>")
def profile(uname):
    user=Users.query.filter_by(username=user).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html")