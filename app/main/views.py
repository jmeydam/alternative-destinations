from flask import render_template, session, redirect, url_for
from ..models import Destination
from . import main
from .forms import ParameterForm

test_url = '../api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=20'


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ParameterForm()
    if form.validate_on_submit():
        #return redirect(url_for('.index'))
        return redirect(test_url)
    return render_template('index.html', form=form)
