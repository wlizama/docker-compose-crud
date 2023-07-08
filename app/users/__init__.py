from flask import Blueprint
from flask_restful import Api
from .resources import UserResource, UserListResource

user_blueprint = Blueprint('users', __name__)
api = Api(user_blueprint)

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
