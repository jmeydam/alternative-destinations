from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, Optional


class ParameterForm(FlaskForm):
    iata_code = StringField(
        'IATA Code of Original Destination', 
        default='LHR',
        validators=[InputRequired(), Length(min=3, max=3)])
    date = DateField(
        'Date of Journey', 
        format='%Y-%m-%d',
         default=datetime.today(),
        validators=[InputRequired()])
    min_temperature_celsius = IntegerField(
        'Minimum Temperature (Degrees Celsius)', 
        default=5,
        validators=[InputRequired(), NumberRange(min=-50, max=50)])
    max_temperature_celsius = IntegerField(
        'Maximum Temperature (Degrees Celsius)', 
        default=20,
        validators=[InputRequired(), NumberRange(min=-50, max=50)])
    max_precipitation_mm = IntegerField(
        'Maximum Precipitation (Millimeters per Hour)', 
        default=0,
        validators=[InputRequired(), NumberRange(min=0, max=50)])
    max_cloud_cover_percent = IntegerField(
        'Maximum Cloud Cover (Percent)', 
        default=20,
        validators=[Optional(), NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')
