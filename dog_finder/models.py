from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# from dog_finder.website import app
# from dog_finder.website import DB_NAME
# from flask_sqlalchemy import SQLAlchemy
# from os import path
# from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

# class User:

#     def __init__(self,db):
#         self.id = db.Column(db.Integer, primary_key=True)
#         self.email = db.Column(db.String(200), unique=True)
#         self.password = db.Column(db.String(150))
#         self.first_name = db.Column(db.String(150))

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

# def init_db():
#     db.create_all()

#     # Create a test user
#     new_user = User('a@a.com', 'aaaaaaaa')
#     new_user.display_name = 'Nathan'
#     db.session.add(new_user)
#     db.session.commit()

    
# def create_database(app):
#     if not path.exists('dog_finder/' + DB_NAME):
#         db.create_all(app=app)
#         # user = User(db)
#         print('created Database')




# if __name__ == '__main__':
#     create_database(app)