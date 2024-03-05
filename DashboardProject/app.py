from flask import Flask, redirect, render_template, request, flash, url_for
from models import User

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/header')
def header():
    return render_template("header.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html")

@app.route('/newAccount')
def newAccount():
    return render_template("newAccount.html")

@app.route('/accountSetting')
def accountSetting():
    return render_template("accountSetting.html")

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/analysis')
def analysis():
    return render_template("analysis.html")



if __name__ == '__main__':
    app.run()
