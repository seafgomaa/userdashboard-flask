from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('')


@auth.route('/logout')
def logout():
    return '<p>Logout</P>'


@auth.route('/signup')
def signup():
    return '<p>Signup</P>'
