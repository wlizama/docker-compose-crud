from flask import jsonify, request
from controllers.user_controller import UserController  # importa la clase UserController desde user_controller.py

class UserView:  # cambia el nombre de la clase a UserView para evitar conflictos de nombres
    def __init__(self):
        self.controller = UserController()  # inicializa UserController desde user_controller.py

    def get_all_users(self):
        users = self.controller.get_all_users()
        return jsonify(users)

    def get_user(self, user_id):
        user = self.controller.get_user(user_id)
        return jsonify(user)

    def create_user(self):
        data = request.get_json()
        user = self.controller.create_user(data)
        return jsonify(user)

    def update_user(self, user_id):
        data = request.get_json()
        user = self.controller.update_user(user_id, data)
        return jsonify(user)

    def delete_user(self, user_id):
        result = self.controller.delete_user(user_id)
        return jsonify(result)
