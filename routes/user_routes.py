from flask import Blueprint
from views.user_views import UserController

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

@user_routes.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_all_users()

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)

@user_routes.route('/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update_user(user_id)

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)
