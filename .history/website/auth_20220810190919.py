from flask import Blueprint, ren

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return '<p>Login</P>'


@auth.route('/logout')
def logout():
    return '<p>Logout</P>'


@auth.route('/signup')
def signup():
    return '<p>Signup</P>'