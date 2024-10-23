  department.py course.py user.py enrollment.py assignment.py submission.py
  from app import db

 class Faculty(db.Model):
    __tablename__ = 'Faculty'
    
    facultyId = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String(50), nullable=False)
    universityId = db.Column(db.Integer, db.ForeignKey('University.universityId'), nullable=False)

    def to_dict(self):
        return {
            'facultyId': self.facultyId,
            'facultyName': self.facultyName,
            'universityId': self.universityId
        }