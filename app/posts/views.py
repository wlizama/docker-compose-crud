from flask_restful import Resource, fields, marshal_with, reqparse
from .models import Post
from app.users.models import User
from database import db

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'user_id': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, help="Title cannot be blank!")
parser.add_argument('content', required=True, help="Content cannot be blank!")
parser.add_argument('user_id', required=True, help="Id is required")

class PostListResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        posts = Post.query.all()
        return posts
        # return {'posts': [post.to_dict() for post in posts]}

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        user_id = args['user_id']
        User.query.filter_by(id=user_id).first_or_404(description='No user found!')
        new_post = Post(title=args['title'], content=args['content'], user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post, 201

class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get(post_id)
        if post is None:
            return {'message': 'Post not found'}, 404
        return post.to_dict()

    def put(self, post_id):
        # Código para actualizar un post existente ...
        pass

    def delete(self, post_id):
        # Código para borrar un post existente ...
        pass
