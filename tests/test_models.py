import unittest
from flask import current_app
from flask.testing import FlaskClient
from sqlalchemy import desc
from app import create_app, db
from app.models import Airport, Destination, Weather


class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Airport.insert_test_airports()
        Destination.insert_test_destinations()
        Weather.insert_test_weather_conditions()

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
        self.assertTrue(len(test_destinations) == 7)

    def test_select_all_weather_conditions(self):
        test_weather_conditions =  Weather.query.all()
        #print(test_weather_conditions)
        self.assertTrue(len(test_weather_conditions) == 3)

    def test_select_single_airport(self):
        test_airport =  Airport.query.filter_by(iata_code='MAD').first()
        #print(test_airport)
        self.assertTrue(test_airport.iata_code == 'MAD')

    def test_select_single_destination(self):
        test_destination =  Destination.query.filter_by(iata_code='MAD').first()
        #print(test_destination)
        self.assertTrue(test_destination.iata_code == 'MAD')

    def test_select_single_weather_condition(self):

        test_weather_condition =  Weather.query.filter_by(
            iata_code='MAD',
            month='January').first()
        #print(test_weather_condition)
        self.assertTrue(
            (test_weather_condition.iata_code == 'MAD') and
            (test_weather_condition.month == 'January'))

    def test_select_single_weather_condition_via_temperatures(self):
        test_weather_condition =  Weather.query.filter(
            Weather.month == 'January',
            Weather.min_temperature_celsius > 10,
            Weather.max_temperature_celsius < 25).first()
        #print(test_weather_condition)
        self.assertTrue(
            (test_weather_condition.iata_code == 'TLV') and
            (test_weather_condition.month == 'January'))

    def test_select_multiple_weather_conditions_via_temperatures(self):
        query =  Weather.query.filter(
            Weather.month == 'January',
            Weather.min_temperature_celsius > 0,
            Weather.max_temperature_celsius < 25).order_by(
                desc(Weather.min_temperature_celsius))
        #print(query)
        #for record in query:
        #    print(record)
        #    print(record.iata_code)
        records = query.all()
        self.assertTrue(records[0].iata_code == 'TLV') 
        self.assertTrue(records[1].iata_code == 'IAH') 
        self.assertTrue(records[2].iata_code == 'MAD') 
