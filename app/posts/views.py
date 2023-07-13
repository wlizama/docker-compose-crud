from flask import request
from flask_restx import Namespace, Resource, fields
from .models import Post
from database import db

ns = Namespace('posts', description='Operaciones de posts')

post_model = ns.model('Post', {
    'id': fields.Integer(readOnly=True, description='Identificador único del Post'),
    'title': fields.String(required=True, description='Titulo del Post'),
    'content': fields.String(required=True, description='Contenido del Post'),
    'user_id': fields.Integer(required=True, description='Identificador único del usuario'),
})

@ns.route('/')
class PostListResource(Resource):
    @ns.marshal_list_with(post_model)
    def get(self):
        posts = Post.query.all()
        return posts

    @ns.expect(post_model)
    @ns.marshal_with(post_model, code=201)
    def post(self):
        post_data = request.json
        new_post = Post(title=post_data['title'], content=post_data['content'], user_id=post_data['user_id'])
        db.session.add(new_post)
        db.session.commit()
        return new_post, 201
    
@ns.route('/<int:post_id>')
@ns.response(404, 'User not found')
@ns.param('post_id', 'The post identifier')
class PostResource(Resource):
    @ns.marshal_with(post_model)
    def get(self, post_id):
        return Post.query.get_or_404(post_id, description='no encontrado')

    def put(self, post_id):
        # Código para actualizar un post existente ...
        pass

    def delete(self, post_id):
        # Código para borrar un post existente ...
        pass
