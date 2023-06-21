import os
from flask import Flask
from config import Config
from routes.user_routes import user_routes

app = Flask(__name__)
app.config.from_object(Config)

# Establecer el puerto a través de la variable de entorno FLASK_RUN_PORT
port = int(os.environ.get('FLASK_RUN_PORT', 5003))

app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

