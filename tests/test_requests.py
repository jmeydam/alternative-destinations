import unittest
from base64 import b64encode
from flask import current_app
from flask.testing import FlaskClient
from werkzeug.datastructures import Headers
from app import create_app, db
from app.models import Airport, Destination


unauthorized_json = b'{\n  "error": "unauthorized", \n  "message": "Invalid credentials"\n}\n'
bad_request_json = b'{\n  "error": "bad request", \n  "message": "Invalid input"\n}\n'
not_found_json = b'{\n  "error": "not found"\n}\n'

# default suggestions with London
default_with_london = b'{"alternative_destinations":\n  [\n    {"iata_code": "CDG", "city": "Paris"},\n    {"iata_code": "LHR", "city": "London"},\n    {"iata_code": "FCO", "city": "Rome"}\n  ]\n}\n'

# default suggestions without London
default_without_london = b'{"alternative_destinations":\n  [\n    {"iata_code": "CDG", "city": "Paris"},\n    {"iata_code": "FCO", "city": "Rome"},\n    {"iata_code": "JFK", "city": "New York"}\n  ]\n}\n'


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

    def test_request_unauthorized(self):
        self.app.testing = True
        client = self.app.test_client()
        with self.app.test_client() as tcl:
            query = '/api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0'
            response = tcl.get(query)
            self.assertTrue(response.status_code == 401) # UNAUTHORIZED
            # brittle, depends on environment
            #test_data_json = response.get_data()
            #self.assertTrue(test_data_json == unauthorized_json)

    def test_request_not_found(self):
        self.app.testing = True
        auth_string = "{0}:{1}".format('user_01', current_app.config['PASSWORD_USER_01'])
        auth_bytes = auth_string.encode('utf-8')
        b64_encoded_auth_bytes = b64encode(auth_bytes)
        headers = Headers()
        headers.add('Authorization',
              'Basic ' + b64_encoded_auth_bytes.decode('utf-8'))
        with self.app.test_client() as tcl:
            query = '/api/v1/XXXXX'
            response = tcl.get(query, headers=headers)
            self.assertTrue(response.status_code == 404) # NOT FOUND
            # brittle, depends on environment
            #test_data_json = response.get_data()
            #self.assertTrue(test_data_json == not_found_json)

    # handled in the same way: exceptions raised at the beginning of 
    # get_alternative_destinations() in module alternative_destinations
    # (in particular, type conversion exceptions and failed asserts)
    def test_request_missing_input(self):
        self.app.testing = True
        auth_string = "{0}:{1}".format('user_01', current_app.config['PASSWORD_USER_01'])
        auth_bytes = auth_string.encode('utf-8')
        b64_encoded_auth_bytes = b64encode(auth_bytes)
        headers = Headers()
        headers.add('Authorization',
              'Basic ' + b64_encoded_auth_bytes.decode('utf-8'))
        with self.app.test_client() as tcl:
            query = '/api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20'
            response = tcl.get(query, headers=headers)
            self.assertTrue(response.status_code == 400) # BAD REQUEST
            # brittle, depends on environment
            #test_data_json = response.get_data()
            #self.assertTrue(test_data_json == bad_request_json)

    def test_request_invalid_iata_code(self):
        self.app.testing = True
        auth_string = "{0}:{1}".format('user_01', current_app.config['PASSWORD_USER_01'])
        auth_bytes = auth_string.encode('utf-8')
        b64_encoded_auth_bytes = b64encode(auth_bytes)
        headers = Headers()
        headers.add('Authorization',
              'Basic ' + b64_encoded_auth_bytes.decode('utf-8'))
        with self.app.test_client() as tcl:
            query = '/api/v1/search?iata_code=XXX&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0'
            response = tcl.get(query, headers=headers)
            test_data_json = response.get_data()
            self.assertTrue(response.status_code == 200) # OK
            self.assertTrue(test_data_json == default_with_london)

    def test_request_london(self):
        self.app.testing = True
        auth_string = "{0}:{1}".format('user_01', current_app.config['PASSWORD_USER_01'])
        auth_bytes = auth_string.encode('utf-8')
        b64_encoded_auth_bytes = b64encode(auth_bytes)
        headers = Headers()
        headers.add('Authorization',
              'Basic ' + b64_encoded_auth_bytes.decode('utf-8'))
        with self.app.test_client() as tcl:
            query = '/api/v1/search?iata_code=LHR&date=2019-01-15&min_temperature_celsius=5&max_temperature_celsius=20&max_precipitation_mm=0'
            response = tcl.get(query, headers=headers)
            test_data_json = response.get_data()
            self.assertTrue(response.status_code == 200) # OK
            self.assertTrue(test_data_json == default_without_london)

    def test_request_london_with_deprecated_param_cloud_cover(self):
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
            test_data_json = response.get_data()
            self.assertTrue(response.status_code == 200) # OK
            self.assertTrue(test_data_json == default_without_london)
