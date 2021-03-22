from datetime import datetime
from api import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password_hash, method='sha256')

    def to_dict(self):
        return dict(
                id=self.id,
                username=self.username,
                email=self.email,
                password_hash=self.password_hash,
                posts=[post.to_dict() for post in self.posts]
                )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return dict(
                id=self.id,
                body=self.body,
                timestamp=self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                user_id=self.user_id
                )
