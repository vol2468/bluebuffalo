from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

def check_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                # flash('Logged in successfully!', category='success')
                return redirect(url_for("auth.dashboard"))
            else:
                flash('Incorrect password, try again.', category='error')
                return render_template("login.html")
        else:
            flash('Email does not exist.', category='error')
            return render_template("login.html")

    return render_template("login.html")
