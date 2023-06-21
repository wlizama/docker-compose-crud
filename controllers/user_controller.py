from models.user import User, db

class UserController:
    def get_all_users(self):
        users = User.query.all()
        return [user.__dict__ for user in users]

    def get_user(self, user_id):
        user = User.query.get(user_id)
        return user.__dict__ if user else {}

    def create_user(self, data):
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return user.__dict__

    def update_user(self, user_id, data):
        user = User.query.get(user_id)
        if user:
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return user.__dict__
        return {}

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}
        return {'message': 'User not found'}
