import os

class Config:
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    SQLALCHEMY_TRACK_MODIFICATIONs = False
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')