from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,PasswordField, ValidationError
from wtforms.validators import Email, EqualTo, Required
from app.models import Users

class Register(FlaskForm):
    username=StringField("Username", validators=[Required()])
    email=StringField("Email", validators=[Required(), Email()])
    password=PasswordField("Password", validators=[Required(),EqualTo("confirm_password", message="Passwords do not match")])
    confirm_password=PasswordField("confirm_password", validators=[Required()])
    submit=SubmitField("Register")

    def validate_email(self, data_field):
        if Users.query.filter_by(email=data_field.data).first():
            raise ValidationError("There is an account with that email")
    
    def validate_username(self, data_field):
        if Users.query.filter_by(username=data_field.data).first():
            raise ValidationError("There is an account with that username")
    
class Login(FlaskForm):
    email=StringField("Username", validators=[Required(), Email()])
    password=PasswordField("Password", validators=[Required()])
    remember=BooleanField("Remember me")
    submit=SubmitField("Sign In")
    
