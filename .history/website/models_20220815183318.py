from . import db
from flask_login import UserMixin
from sqlalchemy import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    email = db.Column(db.String(10000))
    email = db.Column(db.String(10000))
