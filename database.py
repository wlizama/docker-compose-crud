import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

USER_NAME = str(os.environ.get('POSTGRES_USER', ''))
PASSWORD = str(os.environ.get('POSTGRES_PASSWORD', ''))
HOST = str(os.environ.get('POSTGRES_HOST', ''))
PORT = int(os.environ.get('POSTGRES_PORT', 5432))
DATABASE = str(os.environ.get('POSTGRES_DB', ''))
DATABASE_URI = f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"