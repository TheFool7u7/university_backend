  assignment.py submission.py
  from app import db

class Enrollment(db.Model):
    __tablename__ = 'Enrollments'
    
    enrollmentId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(20), db.ForeignKey('Users.userId'), nullable=False)
    courseId = db.Column(db.Integer, db.ForeignKey('Courses.courseId'), nullable=False)
    enrollmentDate = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'enrollmentId': self.enrollmentId,
            'userId': self.userId,
            'courseId': self.courseId,
            'enrollmentDate': self.enrollmentDate
        }