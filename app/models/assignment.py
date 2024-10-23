  submission.py
  from app import db

class Assignment(db.Model):
    __tablename__ = 'Assignments'
    
    assignmentId = db.Column(db.Integer, primary_key=True)
    assignmentTitle = db.Column(db.String(50), nullable=False)
    assignmentDescription = db.Column(db.Text, nullable=False)
    courseId = db.Column(db.Integer, db.ForeignKey('Courses.courseId'), nullable=False)
    dueDate = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'assignmentId': self.assignmentId,
            'assignmentTitle': self.assignmentTitle,
            'assignmentDescription': self.assignmentDescription,
            'courseId': self.courseId,
            'dueDate': self.dueDate
        }