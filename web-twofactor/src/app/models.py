from datetime import datetime
from app import db
from . import pwd_context
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Information to be provided by user
    name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password: str):
        self.password_hash = pwd_context.hash(password, scheme="argon2")


    def verify_password(self, password: str):
        return pwd_context.verify_and_update(password, self.password_hash)

    def __unicode__(self):
        return self.name
