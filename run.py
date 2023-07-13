import os
from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from database import db, DATABASE_URI
from app.users.views import ns as users_ns

PORT = int(os.environ.get('FLASK_RUN_PORT', 5000))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    api = Api(app, version='1.0', title='User API',
              description='A simple User API',
    )
    
    api.add_namespace(users_ns, path='/api')

    db.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=PORT, debug=True)
