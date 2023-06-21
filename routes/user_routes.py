from flask import Blueprint
from views.user_views import UserView  # importa UserView desde user_views.py

user_routes = Blueprint('user_routes', __name__)
user_view = UserView()  # crea una instancia de UserView

# reemplaza 'user_controller' por 'user_view' en las siguientes líneas
@user_routes.route('/users', methods=['GET'])
def get_users():
    return user_view.get_all_users()

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_view.get_user(user_id)

@user_routes.route('/users', methods=['POST'])
def create_user():
    return user_view.create_user()

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_view.update_user(user_id)

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_view.delete_user(user_id)
