from .db import db
from .user import User
from .service_stuff import service_stuff
from .booking_service import booking_service

class Service(db.Model):
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Numeric(6, 2), nullable=False)
    
    stuff = db.relationship('User', secondary=service_stuff, back_populates='services', lazy='joined')
    booking = db.relationship('Booking', secondary=booking_service, back_populates='services', lazy='joined')
    
    def to_dict(self):
        return {
            'id': self.id,
            'service': self.service,
            'price': self.price,
            'stuff': [{'id': user.id, 'email': user.email } for user in self.staff]
        }
