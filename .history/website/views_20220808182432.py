from flask import Blueprint

views = Blueprints('viwes', __name__)

@views.route('/')
