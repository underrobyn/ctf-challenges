from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email


class CreateUserForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message='Please enter a name'),
        Length(min=1, max=50)
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Please enter an email'),
        Email(message='Please enter a valid email')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Please enter a password'),
        Length(min=8, max=255, message='Password does not meet length requirements')
    ])
    submit = SubmitField('Register')


class LoginUserForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Please enter your email'),
        Email(message='Please enter a valid email')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Please enter your password'),
        Length(min=8, max=255, message='Password does not meet length requirements')
    ])
    submit = SubmitField('Login')


class MFAUserForm(FlaskForm):
    code = IntegerField('MFA Code', validators=[
        DataRequired(message='Please enter the 6-digit code from your MFA app')
    ])
    submit = SubmitField('Authorise')
