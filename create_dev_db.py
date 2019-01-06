from flask import current_app
from app import create_app, db
from app.models import User

app = create_app('development')
app_context = app.app_context()
app_context.push()

db.create_all()

user_alice = User(username='alice')
user_bob = User(username='bob')

db.session.add_all([user_alice, user_bob])
db.session.commit()
db.session.remove()

app_context.pop()
