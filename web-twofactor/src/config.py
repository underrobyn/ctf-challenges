from os import environ
from datetime import timedelta


class Config:
    TESTING = environ.get('TESTING')
    DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'adgjuaebg4HRQ34H'

    # https://flask.palletsprojects.com/en/master/config/#SESSION_COOKIE_SECURE
    SESSION_COOKIE_NAME = 'TwoFactorSession'
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'

    REMEMBER_COOKIE_DURATION = timedelta(seconds=1209600)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///./app.db'  # environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
