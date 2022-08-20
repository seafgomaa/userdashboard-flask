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
    if request.method ==''
    email = request.form.get('email')
    name = request.form.get('name')
    passowrd1 = request.form.get('passowrd1')
    password2 = request.form.get('password2')
    if len(email)<4:
        flash('Email must be greater than 3 characters', category='error')
    elif len(name) < 2:
        flash('name must be greater than 1 characters', category='error')
    elif len(passowrd1) < 4:
        flash('password must be greater than 3 characters', category='error')
    elif passowrd1 != password2:
        flash('passwords must match', category='error')
    else:
        flash('Account created successfully!', category='success')    
    return render_template('signup.html')
