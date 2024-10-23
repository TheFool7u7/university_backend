  courses.py assignments.py
  from flask import Blueprint, request, jsonify
from app.models.university import University
from app.models.faculty import Faculty
from app.models.department import Department
from app.models.course import Course
from app import db

bp = Blueprint('academic', __name__)

@bp.route('/universities', methods=['GET'])
def get_universities():
    universities = University.query.all()
    
    return jsonify([u.to_dict() for u in universities]), 200

@bp.route('/faculties', methods=['GET'])
def get_faculties():
    faculties = Faculty.query.all()
    
    return jsonify([f.to_dict() for f in faculties]), 200

@bp.route('/departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    
    return jsonify([d.to_dict() for d in departments]), 200

@bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    
    return jsonify([c.to_dict() for c in courses]), 200