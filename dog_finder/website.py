from flask import Flask
from flask import render_template, request, flash, redirect, url_for, jsonify
from os import path
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user
from dog_finder.models import db, User, Dog_breed
from dog_finder.score_analyzer import calculate_range





app = Flask(__name__)
app.config['SECRET_KEY'] = 'dqddececcad efde'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/dbschema'
db.init_app(app)
app.config.from_pyfile("config.py")


@app.route('/')
def home():
    return render_template('home.html', page_title="Danas Dog Finder")

@app.route('/questionnair', methods=['GET', 'POST'])
@login_required
def questionnair():
    if request.method == "POST":
        # getting input from form for first question
        score = request.json["score"]

        dog_breed = Dog_breed()
        dog_breed_list= dog_breed.query.all()
        result = calculate_range(dog_breed_list, score)
        return jsonify({"score":score,"result": result})
       
    return render_template('questionnair.html', user=current_user, page_title="Questionnair")




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user, page_title="Login")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method== 'POST':
        email= request.form.get('email')
        first_name= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
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
            login_user(new_user, remember=True)
            flash("Account was created", category='success')
            return redirect(url_for('home'))
    

    return render_template('signup.html', user=current_user, page_title="Sign Up")


# @app.route('/score_comp', methods=["POST"])
# def score_comp():
#     # user_score = request.form.get("student_id")
#     # cur = mysql.connection.cursor()
#     # cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,)
#     # conn.commit()
#     # score = request.args.get('score', 0, type=json)
#     return jsonify(score)
#     return string.Format("your score: " + score)
#     print(score)
#     return jsonify(status="success")
#     # return render_template('questionnair.html', user=current_user)    


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))





if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)