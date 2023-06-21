import os
from flask import Flask
from flask_restful import Resource, Api

port = int(os.environ.get('FLASK_RUN_PORT', 5003))
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)