from flask import request, make_response
from flask_cors import cross_origin
from . import api
from .authentication import auth
from app.models import Destination

@api.route('/search')
@auth.login_required
@cross_origin()
def get_alternative_destinations():
    iata_code = request.args.get('iata_code')
    date = request.args.get('date')
    min_temperature_celsius = request.args.get('min_temperature_celsius')
    max_temperature_celsius = request.args.get('max_temperature_celsius')
    max_precipitation_mm = request.args.get('max_precipitation_mm')
    max_cloud_cover_percent = request.args.get('max_cloud_cover_percent')

    # test query:
    # /api/v1/search?iata_code=LHR
    #               &date=2019-01-15
    #               &min_temperature_celsius=5
    #               &max_temperature_celsius=20
    #               &max_precipitation_mm=0
    #               &max_cloud_cover_percent=20

    if (iata_code== 'LHR' and 
        date == '2019-01-15' and 
        min_temperature_celsius == '5' and 
        max_temperature_celsius == '20' and
        max_precipitation_mm == '0' and
        max_cloud_cover_percent == '20'):
        # return test locations
        dest_1 = Destination.query.filter_by(iata_code='MAD').first()
        dest_2 = Destination.query.filter_by(iata_code='TLV').first()
        dest_3 = Destination.query.filter_by(iata_code='IAH').first()
    else:
        dest_1 = '?'
        dest_2 = '?'
        dest_3 = '?'

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
