from . import auth
from flask import render_template, redirect, request,url_for, flash
from ..models import Users
from .forms import Register, Login
from .. import db
from flask_login import login_user

@auth.route("/register", methods=["GET", "POST"])
def register():
    registration=Register()
    if registration.validate_on_submit():
        users=Users(username=registration.username.data, email=registration.email.data, pass_secure=registration.password.data)
        db.session.add(users)
        db.session.commit()
        return redirect("auth.login")
    title="Register"
    return render_template("auth/register.html", title=title, registration=registration)

@auth.route("/login")
def login():
    login_form=Login()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get("next") or url_for("main.index"))
            flash("invalid uersname or password")
    title="Login"
    return render_template("auth/login.html", title=title, login_form=login_form)