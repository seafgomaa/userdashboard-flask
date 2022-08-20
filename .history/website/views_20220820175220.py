from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    note = request.form.get('note')
    if len(note)
    return render_template("home.html" , user=current_user)
