from flask_restful import Resource, fields, marshal_with, reqparse
from database import db
from .models import User

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'age': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank!")
parser.add_argument('email', required=True, help="Email cannot be blank!")
parser.add_argument('age', required=True, help="Age cannot be blank!")

class UserResource(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user

    @marshal_with(resource_fields)
    def put(self, user_id):
        args = parser.parse_args()
        user = User.query.get_or_404(user_id)
        user.name = args['name']
        user.email = args['email']
        user.age = args['age']
        db.session.commit()
        return user

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class UserListResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        new_user = User(name=args['name'], email=args['email'],  age=args['age'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201