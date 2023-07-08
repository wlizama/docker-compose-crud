import os
from flask import Flask
from flask_migrate import Migrate
from database import db, DATABASE_URI
from app.users import user_blueprint
from app.posts import posts_blueprint
from app.comments import comments_blueprint

PORT = int(os.environ.get('FLASK_RUN_PORT', 5000))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(comments_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=PORT, debug=True)
