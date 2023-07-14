from flask import request
from flask_restx import Namespace, Resource, fields
from database import db
from .models import User

ns = Namespace('users', description='Operaciones de usuarios')

user_model = ns.model('User', {
    'id': fields.Integer(readOnly=True, description='Identificador único del usuario'),
    'name': fields.String(required=True, description='Nombre del usuario'),
    'email': fields.String(required=True, description='Email del usuario'),
    'age': fields.Integer(description='Edad de usuario'),
})

@ns.route('')
class UserListResource(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        users = User.query.all()
        return users

    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        user_data = request.json
        new_user = User(name=user_data['name'], email=user_data['email'], age=user_data['age'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201

@ns.route('/<int:user_id>')
@ns.response(404, 'User not found')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    @ns.marshal_with(user_model)
    def get(self, user_id):
        return User.query.get_or_404(user_id)

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json
        user.name = user_data['name']
        user.email = user_data['email']
        user.age = user_data['age']
        db.session.commit()
        return user

    @ns.response(204, 'User deleted')
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

