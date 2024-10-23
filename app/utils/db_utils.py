 
 from app import db

def create_tables():
    db.create_all()

def drop_tables():
    db.drop_all()