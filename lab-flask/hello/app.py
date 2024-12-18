import os
from flask import Flask
from flask_migrate import Migrate

from api.routes import api
from api.commands import setup_commands
from api.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.sqlit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db, compare_type=True)

db.init_app(app)
setup_commands(app)

app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 3030))
    app.run(host='0.0.0.0', port=PORT, debug=True)
