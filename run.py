import os
from flask import Flask
from database import db, DATABASE_URI
from extensions import api, jwt, migrate
from app.users.views import ns as users_ns
from app.posts.views import ns as posts_ns
from app.auth.views import ns as auth_ns

PORT = int(os.environ.get('FLASK_RUN_PORT', 5000))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Cambiar esto!
    
    api.add_namespace(users_ns, path='/users')
    api.add_namespace(posts_ns, path='/posts')
    api.add_namespace(auth_ns, path='/auth')

    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=PORT, debug=True)
