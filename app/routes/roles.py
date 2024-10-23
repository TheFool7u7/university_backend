from flask import Blueprint, request, jsonify
from app.models.role import Role
from app import db

bp = Blueprint('roles', __name__)

@bp.route('/roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    
    return jsonify([r.to_dict() for r in roles]), 200