import os
from flask import Flask
from flask_restful import Api
from database import db, DATABASE_URI
from users.resources import UserResource, UserListResource

PORT = int(os.environ.get('FLASK_RUN_PORT', 5000))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    api = Api(app)
    db.init_app(app)

    api.add_resource(UserResource, '/users/<int:user_id>')
    api.add_resource(UserListResource, '/users')

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=PORT, debug=True)
