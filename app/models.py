from . import db


class Airport(db.Model):
    # "iata_code","lat","long"
    __tablename__ = 'airports'
    id        = db.Column(db.Integer, primary_key=True)
    iata_code = db.Column(db.String(3), unique=True, nullable=False, index=True)
    lat       = db.Column(db.Float, unique=False, nullable=False, index=True)
    long      = db.Column(db.Float, unique=False, nullable=False, index=True)

    def __repr__(self):
        return '<Airport %r>' % self.iata_code

    @staticmethod
    def insert_test_airports():
        # "MAD",40.47193,-3.56264
        a_01 = Airport(
            iata_code='MAD',
            lat=40.47193,   # N 
            long=-3.56264)  # W
        # "TLV",32.0114,34.8867
        a_02 = Airport(
            iata_code='TLV',
            lat=32.0114,    # N 
            long=34.8867)   # E
        # "IAH",29.9844,-95.3414
        a_03 = Airport(
            iata_code='IAH',
            lat=29.9844,    # N
            long=-95.3414)  # W
        db.session.add_all([a_01, a_02, a_03])
        db.session.commit()


class Destination(db.Model):
    # "city","country","iata_code","lat","long"
    __tablename__ = 'destinations'
    id        = db.Column(db.Integer, primary_key=True)
    iata_code = db.Column(db.String(3), unique=True, nullable=False, index=True)
    city      = db.Column(db.String(100), unique=True, nullable=False, index=False)
    country   = db.Column(db.String(100), unique=False, nullable=False, index=True)
    lat       = db.Column(db.Float, unique=False, nullable=False, index=True)
    long      = db.Column(db.Float, unique=False, nullable=False, index=True)

    def __repr__(self):
        return '<Destination %r>' % (self.iata_code + ' - ' + self.city)

    @staticmethod
    def insert_test_destinations():
        # "Paris","France","CDG",49.0128,2.55
        d_01 = Destination(
            iata_code='CDG',
            city='Paris',
            country='France',
            lat=49.0128,    # N
            long=2.55)      # E
        # "London","United Kingdom","LHR",51.4706,-0.46194
        d_02 = Destination(
            iata_code='LHR',
            city='London',
            country='United Kingdom',
            lat=51.4706,    # N
            long=-0.46194)  # W
        # "Rome","Italy","FCO",41.80028,12.23889
        d_03 = Destination(
            iata_code='FCO',
            city='Rome',
            country='Italy',
            lat=41.80028,   # N
            long=12.23889)  # E
        # "New York","United States","JFK",40.6398,-73.7789
        d_04 = Destination(
            iata_code='JFK',
            city='New York',
            country='United States',
            lat=40.6398,    # N
            long=-73.7789)  # W
        # "Madrid","Spain","MAD",40.47193,-3.56264
        d_05 = Destination(
            iata_code='MAD',
            city='Madrid',
            country='Spain',
            lat=40.47193,   # N 
            long=-3.56264)  # W
        # "Tel Aviv","Israel","TLV",32.0114,34.8867
        d_06 = Destination(
            iata_code='TLV',
            city='Tel Aviv',
            country='Israel',
            lat=32.0114,    # N 
            long=34.8867)   # E
        # "Houston","United States","IAH",29.9844,-95.3414
        d_07 = Destination(
            iata_code='IAH',
            city='Houston',
            country='United States',
            lat=29.9844,    # N
            long=-95.3414)  # W
        db.session.add_all([d_01, d_02, d_03, d_04, d_05, d_06, d_07])
        db.session.commit()


class Weather(db.Model):
    # "iata_code","month","min_temperature_celsius","max_temperature_celsius","daily_precipitation_mm"
    __tablename__ = 'weather_conditions'
    id        = db.Column(db.Integer, primary_key=True)
    iata_code = db.Column(db.String(3), unique=False, nullable=False, index=False)
    month     = db.Column(db.String(10), unique=False, nullable=False, index=False)
    min_temperature_celsius = db.Column(db.Float, unique=False, nullable=False, index=True)
    max_temperature_celsius = db.Column(db.Float, unique=False, nullable=False, index=True)
    daily_precipitation_mm  = db.Column(db.Float, unique=False, nullable=False, index=False)
                           
    def __repr__(self):
        return '<Weather %r>' % (self.iata_code + ' ' + self.month)

    @staticmethod
    def insert_test_weather_conditions():
        pass
        # "MAD","January","2.0","12.9","1.6"
        w_01 = Weather(
            iata_code='MAD',
            month='January',
            min_temperature_celsius=2.0,
            max_temperature_celsius=12.9,
            daily_precipitation_mm=1.6)
        # "TLV","January","12.8","22.0","3.3"
        w_02 = Weather(
            iata_code='TLV',
            month='January',
            min_temperature_celsius=12.8,
            max_temperature_celsius=22.0,
            daily_precipitation_mm=3.3)
        # "IAH","January","8.2","19.6","2.4"
        w_03 = Weather(
            iata_code='IAH',
            month='January',
            min_temperature_celsius=8.2,
            max_temperature_celsius=19.6,
            daily_precipitation_mm=2.4)
        db.session.add_all([w_01, w_02, w_03])
        db.session.commit()
