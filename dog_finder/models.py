# from website import db
from flask_login import UserMixin

# class User:

#     def __init__(self,db):
#         self.id = db.Column(db.Interger, primary_key=True)
#         self.email = db.Column(db.String(200), unique=True)
#         self.password = db.Column(db.String(150))
#         self.first_name = db.Column(db.String(150))

# class User(db.Model, UserMixin):

#     id = db.Column(db.Interger, primary_key=True)
#     email = db.Column(db.String(200), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))   