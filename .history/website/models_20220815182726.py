from . import db
from flask_login import UserMixin
from sqlalchemy import func

class User(db.Model, UserMixin):
