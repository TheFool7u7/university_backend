 
 from flask import Blueprint, request, jsonify
from app.models.assignment import Assignment
from app.models.submission import Submission
from app import db

bp = Blueprint('assignments', __name__)

@bp.route('/assignments/<int:assignment_id>/submissions', methods=['GET'])
def get_submissions(assignment_id):
    submissions = Submission.query.filter_by(assignmentId=assignment_id).all()
    
    return jsonify([s.to_dict() for s in submissions]), 200