from flask import Flask
from flask import render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dqddececcad efde'

# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')
def home():
    return render_template('home.html', page_title="Danas Dog Finder")

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
        firstName= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(firstName) < 2:
            flash("First Name must be greater than 2 characters", category='error')
        elif len(password1) < 7:
            flash("Password must be greater than 7 characters", category='error')
        elif password1 != password2:
            flash("Passwords dont match", category='error')
        else:
             flash("Account was created", category='success')
        

    return render_template('signup.html', page_title="Sign Up")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
