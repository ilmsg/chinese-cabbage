from .db import db

service_stuff = db.Table('service_stuff',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('servces.id'), primary_key=True)
)
