# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:PASSWORD@localhost/"
import os

# SQLALCHEMY_DATABASE_URL = "sqlite:///../database.sqlite3"

DB_NAME = os.environ.get('POSTGRES_NAME')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgrespw@localhost:49153"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'

TOKEN_EXPIRE = 36000