from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,PasswordField
from wtforms.validators import Email, EqualTo, Required

class Register(FlaskForm):
    username=StringField("Username", validators=[Required()])
    email=StringField("Email", validators=[Required(), Email()])
    password=PasswordField("Password", validators=[Required(),EqualTo("confirm_password", message="Passwords do not match")])
    confirm_password=PasswordField("confirm_password", validators=[Required()])
    submit=SubmitField("Register")