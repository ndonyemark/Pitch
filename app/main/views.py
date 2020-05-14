from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from ..models import Users, Pitch, Comments
from .forms import PitchesForm, CommentsForm
from .. import db

@main.route("/")
def index():
    
    title="Pitch"
    return render_template("index.html", title=title)

@main.route("/user/<uname>")
def profile(uname):
    user=Users.query.filter_by(username=user).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user=user)

@main.route("/post_pitch")
# @login_required
def post_pitch():
    pitch_form=PitchesForm
    if pitch_form.validate_on_submit():
        pitch=Pitch(title=pitch_form.title.data, pitch=pitch_form.pitch.data, category=pitch_form.category.data,user_id=current_user.id)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for("main.index"))
    
    title="Post Pitch"
    return render_template("pitches/post_pitch.html", title=title)

@main.route("/pitch/<int:id>")
def single_pitch(id=None):
    if id:
        pitch = Pitch.get_single_pitch(id)
        return render_template('pitch.html', pitch=pitch)
    
    return render_template('pitch.html', pitches=pitches)
pitches = Pitch.query.all()
    