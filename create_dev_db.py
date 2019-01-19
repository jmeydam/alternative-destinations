from flask import current_app
from app import create_app, db
from app.models import Airport, Destination

app = create_app('development')
app_context = app.app_context()
app_context.push()

db.create_all()

with open('data/airports.csv', encoding='utf-8') as file:
    for line in file:
        # "iata_code","lat","long"
        # "MAD",40.47193,-3.56264
        line = line.replace('"', '')
        fields = line.split(',')
        a = Airport(
            iata_code=fields[0],
            lat=float(fields[1]),
            long=float(fields[2]))
        db.session.add(a)

db.session.commit()

with open('data/destinations.csv', encoding='utf-8') as file:
    for line in file:
        # "city","country","iata_code","lat","long"
        # "Madrid","Spain","MAD",40.47193,-3.56264
        line = line.replace('"', '')
        fields = line.split(',')
        d = Destination(
            city=fields[0],
            country=fields[1],
            iata_code=fields[2],
            lat=float(fields[3]),
            long=float(fields[4]))
        db.session.add(d)

db.session.commit()

db.session.remove()

app_context.pop()
