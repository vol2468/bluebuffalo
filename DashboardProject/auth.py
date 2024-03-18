from flask import Flask, redirect, render_template, request, flash, url_for, Blueprint
from DashboardProject.analysis import perform_analysis

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

@auth.route('/map')
def map():
    return render_template("map.html")

# @auth.route('/analysis')
# def analysis():
#     return render_template('analysis.html')

@auth.route('/analysis.py', methods=['GET', 'POST'])
def call_compare():
    result = perform_analysis()
    return result

# @auth.route('/analysis')
# def analysis():
#     # Test1
#     # city = 'Tucson'
#     # Test2
#     # city = 'Phoenix'
#     # Test3
#     city = 'Bethel Island'
#     return perform_analysis(city)
#     # return render_template('analysis.html')

@auth.route('/test')
def test():
    return render_template('test.html')
