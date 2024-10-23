from flask import Blueprint, request, jsonify
from app.models.enrollment import Enrollment
from app import db

bp = Blueprint('enrollments', __name__)

@bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    enrollments = Enrollment.query.all()
    
    return jsonify([e.to_dict() for e in enrollments]), 200