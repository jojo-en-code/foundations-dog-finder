from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(900)) 

class Dog_breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    min_score = db.Column(db.Integer)
    max_score = db.Column(db.Integer)






