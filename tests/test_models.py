import unittest
from flask import current_app
from flask.testing import FlaskClient
from app import create_app, db
from app.models import Airport, Destination


class ModelTestCase(unittest.TestCase):
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

    def test_select_all_airports(self):
        test_airports =  Airport.query.all()
        #print(test_airports)
        self.assertTrue(len(test_airports) == 3)

    def test_select_all_destinations(self):
        test_destinations =  Destination.query.all()
        #print(test_destinations)
        self.assertTrue(len(test_destinations) == 3)

    def test_select_particular_airport(self):
        test_airport =  Airport.query.filter_by(iata_code='MAD').first()
        #print(test_airport)
        self.assertTrue(test_airport.iata_code == 'MAD')

    def test_select_particular_destination(self):
        test_destination =  Destination.query.filter_by(iata_code='MAD').first()
        #print(test_destination)
        self.assertTrue(test_destination.iata_code == 'MAD')
