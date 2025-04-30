from app import db
from datetime import datetime
from flask_login import UserMixin

#Define the user up model with: id, username, password and email
class user(db.Model,UserMixin):
    #primary key for user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    #one to many relationship, user can have many recipes
    recipes=db.relationship("recipe", backref="user",lazy=True)
    #setting up the user password
    def set_password(self,password):
        self.password=password
    #check if user passowrod matches stored password
    def check_password(self,password):
        return self.password==password


#define the model to set up the columns of recipe db with: id, title, decription, instructions and date_time
class recipe(db.Model):
    #primary key for recipe
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    description=db.Column(db.Text)
    ingredients=db.Column(db.Text)
    instructions=db.Column(db.Text)
    date_time=db.Column(db.DateTime, default=datetime.utcnow)
    #foreign key connecting recipe to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

