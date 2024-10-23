from flask import Blueprint, request, jsonify
from app.models.assignment import Assignment
from app import db

bp = Blueprint('assignments', __name__)

@bp.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = Assignment.query.all()
    
    return jsonify([a.to_dict() for a in assignments]), 200