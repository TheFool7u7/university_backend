from flask import Blueprint, request, jsonify
from app.models.submission import Submission
from app import db

bp = Blueprint('submissions', __name__)

@bp.route('/submissions', methods=['GET'])
def get_submissions():
    submissions = Submission.query.all()
    
    return jsonify([s.to_dict() for s in submissions]), 200