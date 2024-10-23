  enrollment.py assignment.py submission.py
  from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'Users'
    
    userId = db.Column(db.String(20), primary_key=True)
    userName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    passwordUser = db.Column(db.String(50), nullable=False)
    roleId = db.Column(db.Integer, db.ForeignKey('Roles.roleId'), nullable=False)
    hireDate = db.Column(db.Date)
    specialty = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    entryYear = db.Column(db.Integer)
    studyProgram = db.Column(db.String(50))

    def to_dict(self):
        return {
            'userId': self.userId,
            'userName': self.userName,
            'lastName': self.lastName,
            'email': self.email,
            'roleId': self.roleId, # Agregar el rol
            'hireDate': self.hireDate,
            'specialty': self.specialty,
            'phone': self.phone,
            'entryYear': self.entryYear,
            'studyProgram': self.studyProgram
        }