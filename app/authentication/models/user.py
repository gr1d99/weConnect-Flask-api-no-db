"""User database model"""

from app import BCRYPT, DB
from app.authentication.utils import hashers
from app.db.models.query import Queryset


class User(DB.Model, Queryset):
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String, unique=True)
    password = DB.Column(DB.String)
    roles = DB.relationship('Role', backref='user', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = hashers.make_password(password)

    def check_password(self, raw_password):
        return BCRYPT.check_password_hash(
            self.password, raw_password
        )
