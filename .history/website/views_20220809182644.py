from flask import Blueprint, render_template

views = Blueprint('viwes', __name__)

@views.route('/')
def home():
    return render_template()