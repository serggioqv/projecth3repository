from app import db
from datetime import datetime
from flask_login import UserMixin

class user(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    #one to many relationship
    recipes=db.relationship("recipe", backref="user",lazy=True)
    def set_password(self,password):
        self.password=password
    def check_password(self,password):
        return self.password==password


'method to set up the collumns of recipe db'
class recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    description=db.Column(db.Text)
    ingredients=db.Column(db.Text)
    instructions=db.Column(db.Text)
    date_time=db.Column(db.DateTime, default=datetime.utcnow)
    #connecting recipe to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

