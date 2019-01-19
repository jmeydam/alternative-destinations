from flask import render_template, session, redirect, url_for
from ..models import Destination
from . import main
from .forms import ParameterForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ParameterForm()
    if form.validate_on_submit():
        #print(dir(form))
        #{'iata_code': 'TLV', 'date': datetime.date(2019, 1, 19), 'min_temperature_celsius': 5, 'max_temperature_celsius': 20, 'max_precipitation_mm': 0, 'max_cloud_cover_percent': 20, 'submit': True, 'csrf_token': 'IjJlZmJmNWEwYWIyYzg5NzAyYjIxZTg5ZDUwNGQyZmJlNzA4MmU4NTUi.XEMG8w.FUeSxALCJ4uoF-Bf_ppIC5vJ34w'}
        #print(form.data)
        #print(form.iata_code)
        #print(form.date.data)
        #print(form.min_temperature_celsius.data) 
        #print(form.max_temperature_celsius.data)
        #print(form.max_precipitation_mm.data)
        #print(form.max_cloud_cover_percent.data)
        #test_url = '../api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=20'
        redirect_url = '../api/v1/search' +\
            '?iata_code=' + form.iata_code.data +\
            '&date=' + form.date.data.strftime('%Y-%m-%d') +\
            '&min_temperature_celsius='  + str(form.min_temperature_celsius.data) +\
            '&max_temperature_celsius='  + str(form.max_temperature_celsius.data) +\
            '&max_precipitation_mm=' + str(form.max_precipitation_mm.data) +\
            '&max_cloud_cover_percent=' + str(form.max_cloud_cover_percent.data) # optional
        #http://127.0.0.1:5000/api/v1/search?iata_code=TLV&date=2019-01-19&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=20
        #http://127.0.0.1:5000/api/v1/search?iata_code=TLV&date=2019-01-19&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=None
        return redirect(redirect_url)
    return render_template('index.html', form=form)
