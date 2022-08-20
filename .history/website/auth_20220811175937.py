from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', text=False)


@auth.route('/logout')
def logout():
    return '<p>Logout</P>'


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    data = request.form
    email = data.get('email')
    name = data.get('name')
    passowrd1 = data.get('passowrd1')
    password2 = data.get('password2')
    if len()
    return render_template('signup.html')
