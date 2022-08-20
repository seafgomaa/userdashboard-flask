from flask import Blueprint

views = Blueprint('viwes', __name__)

@views.route('/')
def home():
    return '<h1> Test </h1>'