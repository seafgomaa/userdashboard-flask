from flask import Blueprints

views = blueprints('viwes', __name__)

@views.route('/')