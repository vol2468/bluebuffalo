from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}]'


    from .views import views
    from .app import app

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(app, url_prefix='/')

    # from .models import User
    # from .models import User

    # db.create_all()

    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('Dashboard/scripts/' + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")