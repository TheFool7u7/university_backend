  course.py user.py enrollment.py assignment.py submission.py
  from app import db

class Department(db.Model):
    __tablename__ = 'Department'
    
    departmentId = db.Column(db.Integer, primary_key=True)
    departmentName = db.Column(db.String(50), nullable=False)
    facultyId = db.Column(db.Integer, db.ForeignKey('Faculty.facultyId'), nullable=False)

    def to_dict(self):
        return {
            'departmentId': self.departmentId,
            'departmentName': self.departmentName,
            'facultyId': self.facultyId
        }