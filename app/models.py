from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users(UserMixin, db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255), unique=True,index=True)
    email=db.Column(db.String(255), unique=True, index=True)
    password=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("cannot access the password property")

    @password.setter
    def password(self,password):
        self.password=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password, password)