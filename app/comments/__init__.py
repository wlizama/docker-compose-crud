from flask import Blueprint
from flask_restful import Api
from .resources import CommentResource, CommentListResource

comments_blueprint = Blueprint('comments', __name__)
api = Api(comments_blueprint)

api.add_resource(CommentListResource, '/comments')
api.add_resource(CommentResource, '/comments/<int:comment_id>')
