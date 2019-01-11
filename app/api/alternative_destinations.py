from flask import request
from flask_cors import cross_origin
from . import api
from .authentication import auth


test_response_json = '''{"alternative_destinations":
  [
    {"iata_code": "MAD", "city": "Madrid"},
    {"iata_code": "TLV", "city": "Tel Aviv"},
    {"iata_code": "IAH", "city": "Houston"}
  ]
}
'''

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
    return test_response_json
