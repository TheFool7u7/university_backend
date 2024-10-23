  faculty.py department.py course.py user.py enrollment.py assignment.py submission.py
from app import db

class University(db.Model):
    __tablename__ = 'University'
    
    universityId = db.Column(db.Integer, primary_key=True)
    universityName = db.Column(db.String(50), nullable=False, unique=True)
    creationDate = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'universityId': self .universityId,
            'universityName': self.universityName,
            'creationDate': self.creationDate
        } 