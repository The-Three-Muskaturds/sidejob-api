import os
from db.database import db_url


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret_key")
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_CSRF_PROTECT = False

