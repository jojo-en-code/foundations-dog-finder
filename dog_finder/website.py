from flask import Flask
from flask import render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
import pymysql
# from mysql import mysql
# import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash




db = SQLAlchemy()
DB_NAME = "dbschema.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dqddececcad efde'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[{DB_Name}]'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/dbschema'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db.init_app(app)
# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')
def home():
    return render_template('home.html', page_title="Danas Dog Finder")

@app.route('/questionnair', methods=['GET', 'POST'])
def questionnair():
    if request.method == "POST":
       # getting input from form for first question
       score = request.json["score"]
       print(score)
       
        # getting input from form for second question
    #    second_question = request.form.get("yes_no")
    #    third_question = request.form.get("yes_no")
    #    fourth_question = request.form.get("yes_no") 
       
    return render_template('questionnair.html', page_title="Questionnair")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', page_title="Login")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html', page_title="Logout")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method== 'POST':
        email= request.form.get('email')
        first_name= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(first_name) < 2:
            flash("First Name must be greater than 2 characters", category='error')
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters", category='error')
        elif password1 != password2:
            flash("Passwords dont match", category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # new_user = User(email=email, first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash("Account was created", category='success')
            return redirect(url_for('home'))
    

    return render_template('signup.html', page_title="Sign Up")
    
# def create_database(app):
#     if not path.exists('dog_finder/' + DB_NAME):
        
#         db.create_all(app=app)
#         # User = User(db)
#         print('created Database')

# from dog_finder.models import db
# create_database(app)
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password"
# )

# print(mydb)







if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

from dog_finder.models import User
