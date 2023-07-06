from .model import User
from db import session

def getAllUsers():
    return session.query(User).all()

def createUser(name, email):
    newUser = User(name=name, email=email)
    session.add(newUser)
    session.commit()

def updateUser(name, new_name):
    user = session.query(User).filter_by(name=name).first()
    user.name = new_name
    session.commit()

def deleteUser(name):
    user = session.query(user).filter_by(name=name).first()
    session.delete(user)
    session.commit()
