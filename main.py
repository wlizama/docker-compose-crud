from flask import Flask
from config import Config
from routes.user_routes import user_routes

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run()
