from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()

class create_location_form(FlaskForm):

    title = StringField('City Name', description="Add The City Name")

    latitude = StringField('Latitude:', [
        validators.DataRequired(),

    ], description="Positive Value")

    longitude = StringField('Longitude:', [
        validators.DataRequired(),

    ], description="Negative Value")

    population = IntegerField('Population:', [
        validators.DataRequired(),

    ], description="Add Population Value ")

    submit = SubmitField()

class edit_location_form(FlaskForm):

    title = StringField('City Name', description="Edit The City Name")

    latitude = StringField('Latitude:', [
        validators.DataRequired(),

    ], description=" Positive Value ")

    longitude = StringField('Longitude:', [
        validators.DataRequired(),

    ], description="Negative Value ")

    population = IntegerField('Population:', [
        validators.DataRequired(),

    ], description="Add Population Value ")

    submit = SubmitField()