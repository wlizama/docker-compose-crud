from flask import Blueprint
from flask_restful import Api
from .resources import PostResource, PostListResource

posts_blueprint = Blueprint('posts', __name__)
api = Api(posts_blueprint)

api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
