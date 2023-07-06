from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
       return f"<User(name='{self.name}', email='{self.email}')>"
