import csv
import json
import logging
import os

from flask import Blueprint, render_template, abort, url_for, current_app, jsonify, flash
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Location
from app.songs.forms import csv_upload
from app.map.forms import create_location_form
from werkzeug.utils import secure_filename, redirect
from flask import Response

map = Blueprint('map', __name__,
                        template_folder='templates')

@map.route('/locations', methods=['POST', 'GET'], defaults={"page": 1})
@map.route('/locations/<int:page>', methods=['POST', 'GET'])
@login_required
def browse_locations(page):
    page = page
    per_page = 5
    pagination = Location.query.paginate(page, per_page, error_out=False)
    items = pagination.items

    # browse locations data
    data = Location.query.all()
    titles = [('location', 'Location'), ('registered_on', 'Registered On')]
    add_url = url_for('map.add_locations')
    try:
        return render_template('browse_locations.html',items=items, data=data, pagination=pagination,titles=titles, add_url=add_url)
    except TemplateNotFound:
        abort(404)

@map.route('/locations/new', methods=['GET', 'POST'])
@login_required
def add_locations():
    form = create_location_form()
    if form.validate_on_submit():
        location = Location.query.filter_by(title=form.title.data).first()
        if location is None:
            location = Location(title=form.title.data, longitude=form.longitude.data,
                            latitude=form.latitude.data, population=form.population.data)
            db.session.add(location)
            db.session.commit()
            flash('Congratulations, you added a new location', 'success')
            return redirect(url_for('map.browse_locations_datatables'))
        else:
            flash('Location Already Exists')
            return redirect(url_for('map.browse_locations'))

    return render_template('location_new.html', form=form)


@map.route('/locations/<int:page>')
@login_required
def retrieve_location(user_id):
    user = Location.query.get(user_id)
    return render_template('browse_locations_datatables.html', user=user)

@map.route('/locations_datatables/', methods=['GET'])
def browse_locations_datatables():

    data = Location.query.all()

    try:
        return render_template('browse_locations_datatables.html',data=data)
    except TemplateNotFound:
        abort(404)

@map.route('/api/locations/', methods=['GET'])
def api_locations():
    data = Location.query.all()
    try:
        return jsonify(data=[location.serialize() for location in data])
    except TemplateNotFound:
        abort(404)


@map.route('/locations/map', methods=['GET'])
def map_locations():
    google_api_key = current_app.config.get('GOOGLE_API_KEY')
    try:
        return render_template('map_locations.html',google_api_key=google_api_key)
    except TemplateNotFound:
        abort(404)



@map.route('/locations/upload', methods=['POST', 'GET'])
@login_required
def location_upload():
    form = csv_upload()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        list_of_locations = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                location = Location.query.filter_by(title=row['location']).first()
                if location is None:
                    current_user.locations.append(Location(row['location'],row['longitude'],row['latitude'],row['population']))
                    db.session.commit()
                else:
                    current_user.locations.append(location)
                    db.session.commit()
        return redirect(url_for('map.browse_locations'))

    try:
        return render_template('upload_locations.html', form=form)
    except TemplateNotFound:
        abort(404)