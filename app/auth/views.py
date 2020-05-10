from . import auth
from flask import render_template, redirect, request,url_for
from ..models import Users
from .forms import Register
from .. import db

@auth.route("/register")
def register():
    registration=Register()
    if registration.validate_on_submit():
        users=Users(username=registration.username.data, email=registration.email.data, pass_secure=registration.password.data)
        db.session.add(users)
        db.session.commit()
        return redirect("auth.login")
    title="Register"
    return render_template("auth/regiter.html", title=title, registration=registration)

@auth.route("/login")
def login():

    title="Login"
    return render_template("auth/login.html", title=title)