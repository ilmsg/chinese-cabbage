from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from .models import db
from .api.auth_routes import auth_routes
from .api.user_routes import user_routes

from .config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(user_routes, url_prefix='/api/user')

db.init_app(app)
Migrate(app, db)

CORS(app)

@app.route('/api/docs')
def api_help():
    """Returns all API routes and their doc strings"""
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                  app.view_functions[rule.endpoint].__doc__ ] 
                  for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list
