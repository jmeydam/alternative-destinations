import unittest
from flask import current_app
from app import create_app, db
from app.models import Destination
from app.api.alternative_destinations import test_data_json

test_data_json_comparison_string = '''{"alternative_destinations":
  [
    {"iata_code": "MAD", "city": "Madrid"},
    {"iata_code": "TLV", "city": "Tel Aviv"},
    {"iata_code": "IAH", "city": "Houston"}
  ]
}
'''


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Destination.insert_test_destinations()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_select_all_test_destinations(self):
        test_destinations =  Destination.query.all()
        # print(test_destinations)
        self.assertTrue(len(test_destinations) == 3)

    def test_select_particular_test_destination(self):
        test_destination =  Destination.query.filter_by(iata_code='MAD').first()
        # print(test_destination)
        self.assertTrue(test_destination.iata_code == 'MAD')

    def test_test_data_json(self):
        self.assertTrue(test_data_json == test_data_json_comparison_string)
