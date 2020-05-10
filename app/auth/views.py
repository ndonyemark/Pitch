from . import views
from flask import render_template, redirect, request,url_for
from ..models import Users

@auth.route("/register")
def register():

    title="Register"
    return render_template("auth/regiter.html", title=title)

@auth.route("/login")
def login():

    title="Login"
    return render_template("auth/login.html", title=title)