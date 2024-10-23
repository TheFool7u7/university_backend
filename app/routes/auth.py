  academic.py courses.py assignments.py
  from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.passwordUser  == data['password']:
        return jsonify({
            'userId': user.userId,
            'userName': user.userName,
            'lastName': user.lastName,
            'email': user.email,
            'roleId': user.roleId,  # Agregar el rol
            'hireDate': user.hireDate,
            'specialty': user.specialty,
            'phone': user.phone,
            'entryYear': user.entryYear,
            'studyProgram': user.studyProgram
        }), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    new_user = User(
        userId=data['userId'], 
        userName=data['userName'], 
        lastName=data['lastName'], 
        email=data['email'], 
        passwordUser =data['password'], 
        roleId=data['roleId'],  # Agregar el rol
        hireDate=data['hireDate'], 
        specialty=data['specialty'], 
        phone=data['phone'], 
        entryYear=data['entryYear'], 
        studyProgram=data['studyProgram']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User  created'}), 201