  assignments.py
from flask import Blueprint, request, jsonify
from app.models.course import Course
from app.models.enrollment import Enrollment
from app import db

bp = Blueprint('courses', __name__)

@bp.route('/courses/<int:course_id>/enrollments', methods=['GET'])
def get_enrollments(course_id):
    enrollments = Enrollment.query.filter_by(courseId=course_id).all()
    
    return jsonify([e.to_dict() for e in enrollments]), 200

@bp.route('/courses/<int:course_id>/assignments', methods=['GET'])
def get_assignments(course_id):
    assignments = Assignment.query.filter_by(courseId=course_id).all()
    
    return jsonify([a.to_dict() for a in assignments]), 200