from flask import current_app
from app import create_app, db
from app.models import Airport, Destination

app = create_app('development')
app_context = app.app_context()
app_context.push()

db.create_all()

# airports
# "iata_code","lat","long"
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

# destinations
# "city","country","iata_code","lat","long"
# "Madrid","Spain","MAD",40.47193,-3.56264
d_01 = Destination(
    iata_code='MAD',
    city='Madrid',
    country='Spain',
    lat=40.47193,   # N 
    long=-3.56264)  # W
# "Tel Aviv","Israel","TLV",32.0114,34.8867
d_02 = Destination(
    iata_code='TLV',
    city='Tel Aviv',
    country='Israel',
    lat=32.0114,    # N 
    long=34.8867)   # E
# "Houston","United States","IAH",29.9844,-95.3414
d_03 = Destination(
    iata_code='IAH',
    city='Houston',
    country='United States',
    lat=29.9844,    # N
    long=-95.3414)  # W

db.session.add_all([a_01, a_02, a_03])
db.session.add_all([d_01, d_02, d_03])
db.session.commit()
db.session.remove()

app_context.pop()
