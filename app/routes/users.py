from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    
    return jsonify([u.to_dict() for u in users]), 200