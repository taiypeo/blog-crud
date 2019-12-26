from . import db, login_manager
from flask_login import UserMixin

import base64
import bcrypt
import datetime
import hashlib


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship("BlogPost", back_populates="creator")

    def set_password(self, pwd):
        sha = base64.b64encode(
            hashlib.sha256(pwd.encode()).digest()
        )  # max bcrypt password length is 72 chars, so we can hash the password with a different algorithm first
        self.password = bcrypt.hashpw(sha, bcrypt.gensalt())
    
    def check_password(self, pwd):
        sha = base64.b64encode(hashlib.sha256(pwd.encode()).digest())
        return bcrypt.checkpw(sha, self.password)

    def __repr__(self):
        return f"<User username={self.username}>"


@login_manager.user_loader
def loader(user_id):
    return User.get(user_id)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False, index=True)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    markdown = db.Column(db.Text, nullable=False)

    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    creator = db.relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<BlogPost title={self.title}>"
