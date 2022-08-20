from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>Login</P>'


@auth.route('/logout')
def logout():
    return '<p>logout</P>'


@auth.route('/signup')
def signup():
    return '<p>signup</P>'
