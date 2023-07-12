from database import db
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }

    def __repr__(self):
       return f"<User(name='{self.name}', email='{self.email}')>"
