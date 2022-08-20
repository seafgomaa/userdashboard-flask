from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>Login</P>'


@auth.route('/logout')
def login():
    return '<p>Login</P>'


@auth.route('/signup')
def login():
    return '<p>Login</P>'
