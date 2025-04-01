from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),

)

db = SQLAlchemy(myapp_obj)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(myapp_obj)
from app import routes, models
from app.models import user
@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))
login_manager.init_app(myapp_obj)