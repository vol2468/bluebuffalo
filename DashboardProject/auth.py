from flask import Flask, redirect, render_template, request, flash, url_for, Blueprint
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@auth.route('/header')
def header():
    return render_template("header.html")


@auth.route('/index')
def index():
    return render_template("index.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/newAccount', methods=['GET', 'POST'])
def newAccount():
    if request.method == 'POST':
        firstname = request.form.get('fname')
        lastname = request.form.get('lname')
        email = request.form.get('regEmail')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')

        if len(email) < 4:
            flash('Email is invalid.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 10:
            flash('Passwords must be at least 10 characters.', category='error')
        else:
            new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password1, method='shf22'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account creation successful!', category='success')
            return redirect(url_for('views.home'))
    else:
        return render_template("newAccount.html")


@auth.route('/accountSetting')
def accountSetting():
    return render_template("accountSetting.html")


@auth.route('/map')
def map():
    return render_template("map.html")


@auth.route('/analysis')
def analysis():
    return render_template('analysis.html')
