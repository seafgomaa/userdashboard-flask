from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash 
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login successfully.', category='success')
            else:
                flash('Wrong Password, Try Again', category='error')
        else:
            flash('Email Does Not Exist', category='error')
    return render_template('login.html', text=False)


@auth.route('/logout')
def logout():
    return '<p>Logout</P>'


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already Exist.', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(name) < 2:
            flash('name must be greater than 1 characters', category='error')
        elif len(password1) < 4:
            flash('password must be greater than 3 characters', category='error')
        elif password1 != password2:
            flash('passwords must match', category='error')
        else:
            new_user = User(email=email, name=name,
                        password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')  
            return redirect('/')
    return render_template('signup.html')
