from flask_jwt_extended import create_access_token, create_refresh_token
from repositories import UserRepository


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(self, first_name, last_name, username, email, password):
        return self.user_repo.add_user(first_name, last_name, username, email, password)

    def authenticate_user(self, username, password):
        user = self.user_repo.get_user(username)
        if user and user.check_password(password):
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return access_token, refresh_token
        return None, None
