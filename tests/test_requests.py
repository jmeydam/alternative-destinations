import unittest
from base64 import b64encode
from flask import current_app
from flask.testing import FlaskClient
from werkzeug.datastructures import Headers
from app import create_app, db
from app.models import Airport, Destination


unauthorized_comparison_string = b'{\n  "error": "unauthorized", \n  "message": "Invalid credentials"\n}\n'

test_data_comparison_string = b'{"alternative_destinations":\n  [\n    {"iata_code": "MAD", "city": "Madrid"},\n    {"iata_code": "TLV", "city": "Tel Aviv"},\n    {"iata_code": "IAH", "city": "Houston"}\n  ]\n}\n'


class RequestTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Airport.insert_test_airports()
        Destination.insert_test_destinations()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_unauthorized_request(self):
        self.app.testing = True
        client = self.app.test_client()
        with self.app.test_client() as tcl:
            query = '/api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=20'
            response = tcl.get(query)
            self.assertTrue(response.status_code == 401) # UNAUTHORIZED
            test_data_json = response.get_data()
            #print(test_data_json)
            self.assertTrue(test_data_json == unauthorized_comparison_string)

    def test_test_data_json(self):
        self.app.testing = True
        auth_string = "{0}:{1}".format('user_01', current_app.config['PASSWORD_USER_01'])
        auth_bytes = auth_string.encode('utf-8')
        b64_encoded_auth_bytes = b64encode(auth_bytes)
        headers = Headers()
        headers.add('Authorization',
              'Basic ' + b64_encoded_auth_bytes.decode('utf-8'))
        with self.app.test_client() as tcl:
            query = '/api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0&max_cloud_cover_percent=20'
            response = tcl.get(query, headers=headers)
            #print(response.get_data())
            test_data_json = response.get_data()
            self.assertTrue(response.status_code == 200) # OK
            self.assertTrue(test_data_json == test_data_comparison_string)
