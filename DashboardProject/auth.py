from flask import Flask, redirect, render_template, request, flash, url_for, Blueprint
from DashboardProject.analysis import perform_analysis
from DashboardProject.map import perform_map

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



@auth.route('/newAccount')
def newAccount():
    return render_template("newAccount.html")


@auth.route('/accountSetting')
def accountSetting():
    return render_template("accountSetting.html")


@auth.route('/map', methods=['GET', 'POST'])
def map():
    result = perform_map()
    return result

@auth.route('/map_test')
def map_test():
    return render_template('map_test.html')

@auth.route('/analysis', methods=['GET', 'POST'])
def call_compare():
    result = perform_analysis()
    return result

@auth.route('/test')
def test():
    return render_template('test.html')

