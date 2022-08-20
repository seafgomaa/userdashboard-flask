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
    if len(email)<4:
        flash('Email must be greater than 3 characters', category='error')
    elif len(name) < 2:
        flash('name must be greater than 1 characters', category='error')
    elif len(passowrd1) < 4:
        flash('password must be greater than 3 characters', category='error')
    elif passowrd1 != password2:
        flash('passwords must match', category='error')
    else:
        flash('Account created succesfully!', category=)    
    return render_template('signup.html')
