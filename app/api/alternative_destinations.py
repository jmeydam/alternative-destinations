from datetime import datetime
from sqlalchemy import desc
from flask import request, make_response
from flask_cors import cross_origin
from . import api
from .authentication import auth
from app.models import Airport, Destination, Weather


MONTH_NAMES = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'}


@api.route('/search')
@auth.login_required
@cross_origin()
def get_alternative_destinations():

    # print(request.args)
    # ImmutableMultiDict([('iata_code', 'LHR'), 
    #                     ('date', '2019-01-15'), 
    #                     ('min_temperature_celsius', '5'), 
    #                     ('max_temperature_celsius', '20'), 
    #                     ('max_precipitation_mm', '0')])

    iata_code = request.args.get('iata_code')
    date = datetime.strptime(request.args.get('date'), '%Y-%m-%d')
    min_temperature_celsius = float(request.args.get('min_temperature_celsius'))
    max_temperature_celsius = float(request.args.get('max_temperature_celsius'))
    max_precipitation_mm = float(request.args.get('max_precipitation_mm'))

    # get three default destinations different from destination of query
    # options: Paris, London, Rome, New York
    default_options = ['CDG', 'LHR', 'FCO', 'JFK'] 
    if iata_code in default_options:
        default_options.remove(iata_code)
    else:
        default_options.remove('JFK')

    dest = []
    dest.append(Destination.query.filter_by(iata_code=default_options[0]).first())
    dest.append(Destination.query.filter_by(iata_code=default_options[1]).first())
    dest.append(Destination.query.filter_by(iata_code=default_options[2]).first())

    #query_airport = Airport.query.filter_by(iata_code=iata_code).first()
    #if query_airport is not None:

    query_weather =  Weather.query.filter(
        Weather.month == MONTH_NAMES[date.month],
        Weather.min_temperature_celsius >= min_temperature_celsius,
        Weather.max_temperature_celsius <= max_temperature_celsius).order_by(
            desc(Weather.min_temperature_celsius))
    for index, weather in enumerate(query_weather):
        if index > 2:
            break
        dest[index] = Destination.query.filter_by(iata_code=weather.iata_code).first()

    line_1 = '{"alternative_destinations":\n'
    line_2 = '  [\n'
    line_3 = '    {"iata_code": "%s", "city": "%s"},\n' % (dest[0].iata_code, dest[0].city)
    line_4 = '    {"iata_code": "%s", "city": "%s"},\n' % (dest[1].iata_code, dest[1].city)
    line_5 = '    {"iata_code": "%s", "city": "%s"}\n'  % (dest[2].iata_code, dest[2].city)
    line_6 = '  ]\n'
    line_7 = '}\n'

    response_string = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7
    response = make_response(response_string)
    response.mimetype = 'application/json'
    return response
