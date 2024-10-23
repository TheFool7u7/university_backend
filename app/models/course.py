  user.py enrollment.py assignment.py submission.py
  from app import db

class Course(db.Model):
    __tablename__ = 'Courses'
    
    courseId = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(50), nullable=False, unique=True)
    courseName = db.Column(db.String(50), nullable=False)
    departmentId = db.Column(db.Integer, db.ForeignKey('Department.departmentId'), nullable=False)

    def to_dict(self):
        return {
            'courseId': self.courseId,
            'courseCode': self.courseCode,
            'courseName': self.courseName,
            'departmentId': self.departmentId
        }