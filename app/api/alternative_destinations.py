from flask import request, make_response
from flask_cors import cross_origin
from . import api
from .authentication import auth
from app.models import Airport, Destination, Weather

@api.route('/search')
@auth.login_required
@cross_origin()
def get_alternative_destinations():

    # print(request.args)
    # ImmutableMultiDict([('iata_code', 'LHR'), 
    #                     ('date', '2019-01-15'), 
    #                     ('min_temperature_celsius', '5'), 
    #                     ('max_temperature_celsius', '20'), 
    #                     ('max_precipitation_mm', '0'), 
    #                     ('max_cloud_cover_percent', '20')])

    iata_code = request.args.get('iata_code')
    date = request.args.get('date')
    min_temperature_celsius = request.args.get('min_temperature_celsius')
    max_temperature_celsius = request.args.get('max_temperature_celsius')
    max_precipitation_mm = request.args.get('max_precipitation_mm')
    max_cloud_cover_percent = request.args.get('max_cloud_cover_percent')

    # get three default destinations different from destination of query
    # options: Paris, London, Rome, New York
    default_options = ['CDG', 'LHR', 'FCO', 'JFK'] 
    if iata_code in default_options:
        default_options.remove(iata_code)
    else:
        default_options.remove('JFK')

    dest_1 = Destination.query.filter_by(iata_code=default_options[0]).first()
    dest_2 = Destination.query.filter_by(iata_code=default_options[1]).first()
    dest_3 = Destination.query.filter_by(iata_code=default_options[2]).first()

    query_airport = Airport.query.filter_by(iata_code=iata_code).first()
    if query_airport is not None:
       pass

    #print('Number of destinations in database:')
    #print(len(Destination.query.all()))
    #print(dir(Destination.query))
    #print('First destination record in database:')
    #print(Destination.query.first())

    line_1 = '{"alternative_destinations":\n'
    line_2 = '  [\n'
    line_3 = '    {"iata_code": "%s", "city": "%s"},\n' % (dest_1.iata_code, dest_1.city)
    line_4 = '    {"iata_code": "%s", "city": "%s"},\n' % (dest_2.iata_code, dest_2.city)
    line_5 = '    {"iata_code": "%s", "city": "%s"}\n'  % (dest_3.iata_code, dest_3.city)
    line_6 = '  ]\n'
    line_7 = '}\n'

    response_string = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7
    response = make_response(response_string)
    response.mimetype = 'application/json'
    return response
