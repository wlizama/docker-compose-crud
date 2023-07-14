from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token

ns = Namespace('auth', description='Autenticación del usuario')

# Definición del modelo para datos entrantes
login_model = ns.model('Login', {
    'username': fields.String(required=True, description='nombre de usuario'),
    'password': fields.String(required=True, description='contraseña del usuario')
})

# Definición del modelo para la respuesta
token_model = ns.model('Token', {
    'access_token': fields.String(description='Token de acceso JWT')
})

@ns.route('')
class UserLogin(Resource):
    @ns.expect(login_model, validate=True)  # Validación de datos entrantes
    @ns.marshal_with(token_model)  # Formateo de la respuesta
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        # Asegúrate de cambiar esta validación con la lógica de tu base de datos.
        if username != 'test' or password != 'test':
            return ns.abort(401, 'Invalid credentials')

        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200
