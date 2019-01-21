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


# get three default destinations different from original destination of query
def default_destinations(iata_code_original_destination):
    # Paris, London, Rome, New York
    defaults = ['CDG', 'LHR', 'FCO', 'JFK'] 
    if iata_code_original_destination in defaults:
        defaults.remove(iata_code_original_destination)
    else:
        defaults.remove('JFK')
    return defaults


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

    #print(Airport.query.filter_by(iata_code=iata_code).first())

    defaults = default_destinations(iata_code)

    dests = []
    dests.append(Destination.query.filter_by(iata_code=defaults[0]).first())
    dests.append(Destination.query.filter_by(iata_code=defaults[1]).first())
    dests.append(Destination.query.filter_by(iata_code=defaults[2]).first())

    query_weather_strict =  Weather.query.filter(
        Weather.month == MONTH_NAMES[date.month],
        Weather.iata_code != iata_code,
        Weather.min_temperature_celsius >= min_temperature_celsius,
        Weather.max_temperature_celsius <= max_temperature_celsius,
        Weather.daily_precipitation_mm  <= max_precipitation_mm).order_by(
            desc(Weather.min_temperature_celsius))
    # print(query_weather_strict)

    result_strict = query_weather_strict.all()
    # print('Strict search found ' + str(len(result_strict)) + ' destinations.')
    # print(result_strict)

    query_weather_fuzzy =  Weather.query.filter(
        Weather.month == MONTH_NAMES[date.month],
        Weather.iata_code != iata_code,
        Weather.min_temperature_celsius >= min_temperature_celsius - 5,
        Weather.max_temperature_celsius <= max_temperature_celsius + 5,
        Weather.daily_precipitation_mm  <= max_precipitation_mm + 5).order_by(
            desc(Weather.min_temperature_celsius))

    result_fuzzy = query_weather_fuzzy.all()
    # print('Fuzzy search found ' + str(len(result_fuzzy)) + ' destinations.')
    # print(result_fuzzy)

    # print(type(result_fuzzy))
    # <class 'list'>

    # append unordered result of fuzzy search to ordered result of strict search
    # only append elements that are not part of the strict search result

    result = result_strict + list(set(result_fuzzy) - set(result_strict))
    # print('Found ' + str(len(result)) + ' destinations. (Results strict search first.)')
    # print(result)

    # overwrite default destinations with search result
    for index, weather in enumerate(result):
        if index > 2:
            break
        dests[index] = Destination.query.filter_by(iata_code=weather.iata_code).first()

    line_1 = '{"alternative_destinations":\n'
    line_2 = '  [\n'
    line_3 = '    {"iata_code": "%s", "city": "%s"},\n' % (dests[0].iata_code, dests[0].city)
    line_4 = '    {"iata_code": "%s", "city": "%s"},\n' % (dests[1].iata_code, dests[1].city)
    line_5 = '    {"iata_code": "%s", "city": "%s"}\n'  % (dests[2].iata_code, dests[2].city)
    line_6 = '  ]\n'
    line_7 = '}\n'

    response_string = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7
    response = make_response(response_string)
    response.mimetype = 'application/json'
    return response
