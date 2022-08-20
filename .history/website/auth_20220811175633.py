from flask import Blueprint, render_template, request

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
    email = data.get('email')
    email = data.get('email')
    email = data.get('email')
    return render_template('signup.html')