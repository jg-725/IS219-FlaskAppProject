from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class login_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])
    submit = SubmitField()


class register_form(FlaskForm):
    email = EmailField('Enter An Email Address', [
        validators.DataRequired(),

    ], description="You need to signup with a valid email")

    password = PasswordField('Create A Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35),
        validators.EqualTo('confirm', message='Passwords did NOT match, Please Try Again!')


    ], description="Create a password with 6 characters or more ")

    confirm = PasswordField('Re-enter Your Password', description="Please retype your password to confirm it is correct")
    submit = SubmitField()


class profile_form(FlaskForm):
    about = TextAreaField('About Me', [validators.length(min=6, max=300)],
                          description="Please add information about yourself")

    submit = SubmitField()

class user_edit_form(FlaskForm):
    about = TextAreaField('About', [validators.length(min=6, max=300)],
                          description="Please add information about yourself")
    is_admin = BooleanField('Admin', render_kw={'value':'1'})
    submit = SubmitField()


class security_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ], description="You can change your email address")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),

    ], description="Type A New Password ")
    confirm = PasswordField('Repeat Password', description="Retype your new password to confirm it is correct!")

    submit = SubmitField()