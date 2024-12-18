from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), default=False)
    
    def __repr__(self):
        return f'<User(id={self.id}, email={self.email})>'
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }