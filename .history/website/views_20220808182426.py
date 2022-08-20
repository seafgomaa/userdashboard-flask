from flask import Blueprints

views = Blueprints('viwes', __name__)

@views.route('/')
