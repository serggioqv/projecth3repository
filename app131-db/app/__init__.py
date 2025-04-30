from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

#Import and create the flask object
myapp_obj = Flask(__name__)

#absolute path of working directory
basedir =os.path.abspath(os.path.dirname(__file__))

# configuration of my project
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess-secret-dont-tell-anyone',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),

)

#setting up the Sqlalchemy database object
db = SQLAlchemy(myapp_obj)
#initizlizing login_manager, configuration
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(myapp_obj)
#import applications and models
from app import routes, models
from app.models import user
#user loader callback for login
@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))
login_manager.init_app(myapp_obj)