from flask import jsonify, request
# from controllers.user_controller import UserController

class UserController:
    def __init__(self):
        pass
        # self.controller = UserController()

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
