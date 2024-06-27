from models import User
from extensions import db


class UserRepository:
    def add_user(self, username, password):
        if User.query.filter_by(username=username).first():
            return False
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return True

    def get_user(self, username):
        return User.query.filter_by(username=username).first()
