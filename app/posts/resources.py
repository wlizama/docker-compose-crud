from flask_restful import Resource
from .models import Post

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return {'posts': [post.to_dict() for post in posts]}

    def post(self):
        # Código para crear un nuevo post ...
        pass

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
