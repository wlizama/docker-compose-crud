import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER_NAME = str(os.environ.get('POSTGRES_USER', ''))
PASSWORD = str(os.environ.get('POSTGRES_PASSWORD', ''))
HOST = str(os.environ.get('POSTGRES_HOST', ''))
PORT = int(os.environ.get('POSTGRES_PORT', 5432))
DATABASE = str(os.environ.get('POSTGRES_DB', ''))

engine = create_engine(f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
Session = sessionmaker(bind=engine)
session = Session()
