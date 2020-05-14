from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))

class Users(UserMixin, db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255), unique=True, index=True)
    pass_secure=db.Column(db.String(255))
    pitches=db.relationship("Pitch", backref='user', lazy="dynamic")
    comments=db.relationship("Comments", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return self;

class Pitch(db.Model):
    __table__name='pitch'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    pitch=db.Column(db.Text)
    category=db.Column(db.String(255))
    date_posted=db.Column(db.DateTime, default=datetime.utcnow)
    users_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.relationship("Comments", backref="pitch")

    @classmethod
    def get_single_pitch(cls, pitch_id):
        pitch = Pitch.query.filter_by(id=pitch_id).first()
        return pitch
    
    @classmethod
    def user_pitches(cls, user_id):
        pitch = Pitch.query.filter_by(users_id=user_id).all()
        return pitch

    # @classmethod
    # def get_single_pitch(cls,id):
    #     pitch=Pitch.query.all()
    #     return pitch

    # @classmethod
    # def get_pitches(cls):
    #     pitch=Pitch.query.all()
    #     return pitch
    
    # @classmethod
    # def get_user_pitch(cls, id):
    #     user_pitch=Pitch.query.filter_by(users_id=id).all()
    #     return user_pitch
    
    # @classmethod
    # def get_pitch_category(cls, category):
    #     category=Pitch.query.filter_by(category=category)
    #     return category

class Comments(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.Text)
    pitch_id=db.Column(db.Integer, db.ForeignKey("pitch.id"))
    # author=db.Column(db.String(40))
    users_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    date_posted=db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def get_pitch(cls,id):
        comments=Comments.query.filter_by(pitch_id).all()
        return comments