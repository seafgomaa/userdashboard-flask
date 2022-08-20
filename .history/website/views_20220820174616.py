from crypt import methods
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['Get'])
@login_required
def home():
    return render_template("home.html" , user=current_user)
