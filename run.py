import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from database import db, DATABASE_URI
from app.users.resources import UserResource, UserListResource
from app.posts.resources import PostResource, PostListResource
from app.comments.resources import CommentResource, CommentListResource

PORT = int(os.environ.get('FLASK_RUN_PORT', 5000))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    api = Api(app)
    db.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(UserResource, '/users/<int:user_id>')
    api.add_resource(UserListResource, '/users')

    api.add_resource(PostListResource, '/posts')
    api.add_resource(PostResource, '/posts/<int:post_id>')
    api.add_resource(CommentListResource, '/comments')
    api.add_resource(CommentResource, '/comments/<int:comment_id>')

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=PORT, debug=True)
