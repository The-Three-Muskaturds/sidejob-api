from models import User
from extensions import db


class UserRepository:
    def add_user(self, first_name, last_name, username, email, password):
        if User.query.filter_by(username=username).first():
            return False
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )
        db.session.add(user)
        db.session.commit()
        return True

    def get_user(self, username):
        return User.query.filter_by(username=username).first()
