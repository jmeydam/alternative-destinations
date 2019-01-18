from flask import current_app
from app import create_app, db
from app.models import Destination

app = create_app('development')
app_context = app.app_context()
app_context.push()

db.create_all()

# "city","country","iata_code","lat","long"
# "Madrid","Spain","MAD",40.47193,-3.56264
dest_01 = Destination(
    iata_code='MAD',
    city='Madrid',
    country='Spain',
    lat=40.47193,   # N 
    long=-3.56264)  # W
# "Tel Aviv","Israel","TLV",32.0114,34.8867
dest_02 = Destination(
    iata_code='TLV',
    city='Tel Aviv',
    country='Israel',
    lat=32.0114,    # N 
    long=34.8867)   # E
# "Houston","United States","IAH",29.9844,-95.3414
dest_03 = Destination(
    iata_code='IAH',
    city='Houston',
    country='United States',
    lat=29.9844,    # N
    long=-95.3414)  # W

db.session.add_all([dest_01, dest_02, dest_03])
db.session.commit()
db.session.remove()

app_context.pop()
