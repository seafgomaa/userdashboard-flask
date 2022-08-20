from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    data = request.form
    print(data)
    return render_template('login.html', text=False)


@auth.route('/logout')
def logout():
    return '<p>Logout</P>'


@auth.route('/signup')
def signup():
    return render_template('signup.html')
