from database import db
# from sqlalchemy.sql.expression import text
# from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    # created_at = db.Column(TIMESTAMP(timezone=True),
    #                     nullable=False, server_default=text('now()'))

    def __repr__(self):
       return f"<User(name='{self.name}', email='{self.email}')>"
