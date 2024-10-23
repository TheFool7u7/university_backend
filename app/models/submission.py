 
 from app import db

class Submission(db.Model):
    __tablename__ = 'Submissions'
    
    submissionId = db.Column(db.Integer, primary_key=True)
    assignmentId = db.Column(db.Integer, db.ForeignKey('Assignments.assignmentId'), nullable=False)
    userId = db.Column(db.String(20), db.ForeignKey('Users.userId'), nullable=False)
    submissionDate = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            'submissionId': self.submissionId,
            'assignmentId': self.assignmentId,
            'userId': self.userId,
            'submissionDate': self.submissionDate,
            'grade': self.grade
        }