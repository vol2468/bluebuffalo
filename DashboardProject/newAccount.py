from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
...
def check_newAccount():
    # code to validate and add user to database goes here
    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if pass1 != pass2:
        flash('Password and confirm password need to be exact same', category='error')
        return redirect(url_for('auth.newAccount'))

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists', category='error')
        return redirect(url_for('auth.login'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(firstName=firstname, lastName=lastname, email=email, password=generate_password_hash(pass1, method='pbkdf2:sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return email