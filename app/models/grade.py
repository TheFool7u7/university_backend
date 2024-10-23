from app import db

class Grade(db.Model):
    __tablename__ = 'Grades'
    
    gradeId = db.Column(db.Integer, primary_key=True)
    gradeName = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'gradeId': self.gradeId,
            'gradeName': self.gradeName
        }