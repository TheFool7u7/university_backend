from app import db

class Role(db.Model):
    __tablename__ = 'Roles'
    
 roleId = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'roleId': self.roleId,
            'roleName': self.roleName
        }