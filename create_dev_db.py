from flask import current_app
from app import create_app, db
from app.models import Destination

app = create_app('development')
app_context = app.app_context()
app_context.push()

db.create_all()

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
db.session.remove()

app_context.pop()
