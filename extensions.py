from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(version='1.0', title='User API',
          description='A simple User API',
          prefix='/api',
          # security='Bearer Auth',  # Define security globally for your API
          authorizations=authorizations
)
jwt = JWTManager()
migrate = Migrate()
