from flask import Blueprint, request, jsonify
from app.models.grade import Grade
from app import db

bp = Blueprint('grades', __name__)

@bp.route('/grades', methods=['GET'])
def get_grades():
    grades = Grade.query.all()
    
    return jsonify([g.to_dict() for g in grades]), 200