from flask import jsonify, current_app
from api import db
from api.main import bp
from api.models import User, Post


@bp.route('/', methods=['GET'])
def index():
    users = User.query.all()
    
    return jsonify({ 'Users': [u.to_dict() for u in users] })
