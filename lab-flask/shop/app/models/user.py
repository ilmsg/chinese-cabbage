from .db import db

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    shops = db.relationship('Shop', secondary='shop', back_populates='user', lazy='dynamic')