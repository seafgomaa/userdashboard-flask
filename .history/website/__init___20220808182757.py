from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'seaf'

    from .views import views
    from .views import views
    return app