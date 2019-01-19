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
    mad = Destination.query.filter_by(iata_code='MAD').first()
    tlv = Destination.query.filter_by(iata_code='TLV').first()
    iah = Destination.query.filter_by(iata_code='IAH').first()
    line_1 = '{"alternative_destinations":\n'
    line_2 = '  [\n'
    line_3 = '    {"iata_code": "%s", "city": "%s"},\n' % (mad.iata_code, mad.city)
    line_4 = '    {"iata_code": "%s", "city": "%s"},\n' % (tlv.iata_code, tlv.city)
    line_5 = '    {"iata_code": "%s", "city": "%s"}\n' % (iah.iata_code, iah.city)
    line_6 = '  ]\n'
    line_7 = '}\n'
    response_string = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7
    response = make_response(response_string)
    response.mimetype = 'application/json'
    return response
