from .db import db
from .booking_service import booking_service

class Booking(db.Model):
    __tablename__ = 'booking'
    
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)

    services = db.relationship('Service', secondary='booking_service', back_populates='booking', lazy='dynamic')
