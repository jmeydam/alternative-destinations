from . import db


class Destination(db.Model):
    __tablename__ = 'destinations'
    id        = db.Column(db.Integer, primary_key=True)
    iata_code = db.Column(db.String(3), unique=True, nullable=False, index=False)
    city      = db.Column(db.String(30), unique=True, nullable=False, index=False)
    region    = db.Column(db.String(20), unique=False, nullable=False, index=True)
    lat       = db.Column(db.Float, unique=False, nullable=False, index=True)
    long      = db.Column(db.Float, unique=False, nullable=False, index=True)

    def __repr__(self):
        return '<Destination %r>' % (self.iata_code + ' - ' + self.city)

    @staticmethod
    def insert_test_destinations():
        dest_01 = Destination(
            iata_code='MAD',
            city='Madrid',
            region='Europe',
            # 40.4983 N, 3.5676 W
            lat=40.4983, 
            long=-3.5676)
        dest_02 = Destination(
            iata_code='TLV',
            city='Tel Aviv',
            region='Middle East',
            # 32.0055 N, 34.8854 E
            lat=32.0055, 
            long=34.8854)
        dest_03 = Destination(
            iata_code='IAH',
            city='Houston',
            region='North America',
            # 29.9902 N, 95.3368 W
            lat=29.9902, 
            long=-95.3368)
        db.session.add_all([dest_01, dest_02, dest_03])
        db.session.commit()
