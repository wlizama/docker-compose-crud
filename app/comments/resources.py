from flask_restful import Resource
from .models import Comment

class CommentListResource(Resource):
    def get(self):
        comments = Comment.query.all()
        return {'comments': [comment.to_dict() for comment in comments]}

    def post(self):
        # Código para crear un nuevo comentario ...
        pass

class CommentResource(Resource):
    def get(self, comment_id):
        comment = Comment.query.get(comment_id)
        if comment is None:
            return {'message': 'Comment not found'}, 404
        return comment.to_dict()

    def put(self, comment_id):
        # Código para actualizar un comentario existente ...
        pass

    def delete(self, comment_id):
        # Código para borrar un comentario existente ...
        pass
