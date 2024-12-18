from flask import Flask, Blueprint, jsonify
from flask_cors import CORS

api = Blueprint('api', __name__)

CORS(api)

@api.route('/hello', methods=['GET', 'POST'])
def hello():
    res_body = {
        "message": "hello."
    }
    
    return jsonify(res_body), 200