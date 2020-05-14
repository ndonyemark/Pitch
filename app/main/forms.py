from ..models import Users, Pitch
from . import forms
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import Required

class PitchesForm(FlaskForm):
    title=StringField("title", validators=[Required()])
    pitch=TextAreaField("Pitch", validators=[Required()])
    category=SelectField("Choose category", choices=[("pickup-lines", "pickup-lines"), ("Technology", "Technology"), ("Business", "Business"), ("lifestyle", "lifestyle"), ("funny", "funny")], validate_choice=True, validators=[Required()])
    submit=SubmitField("Post-Pitch")

class CommentsForm(FlaskForm):
    comment=TextAreaField("Comment", validators=[Required()])