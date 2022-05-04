from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()

class create_location_form(FlaskForm):

    title = StringField('City Name', description="Add The City Name")

    longitude = IntegerField('Longitude:', [
        validators.DataRequired(),

    ], description="Add Longitude Value ")

    latitude = IntegerField('Latitude:', [
        validators.DataRequired(),

    ], description="Add Latitude Value ")

    population = IntegerField('Population:', [
        validators.DataRequired(),

    ], description="Add Population Value ")

    submit = SubmitField()