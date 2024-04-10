from flask import render_template, request, Blueprint, redirect, url_for, flash
from DashboardProject.analysis import perform_analysis, get_latitude, get_longitude, get_mean_values, get_total_mean, get_prediction
from DashboardProject.dashboard import get_top10_data, get_least10_data, get_pollutant_data, get_aqi_population
from DashboardProject.map import perform_map
from DashboardProject.insertComment import insert_comment
from DashboardProject.displayIndexComment import display_comment_index
from DashboardProject.login import check_login
from DashboardProject.logout import check_logout
from flask_login import current_user
from werkzeug.security import generate_password_hash
from DashboardProject.newAccount import check_newAccount
from . import db
from .models import Comment, User
from DashboardProject.message import email_alert
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth', __name__)
@auth.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@auth.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    user_date = request.args.get('date', '2020-01-01')
    top_cities = get_top10_data(user_date)
    least_cities = get_least10_data(user_date)
    pollutant = get_pollutant_data(user_date)
    aqi_population = get_aqi_population(user_date)
    comment = display_comment_index(user_date)
    return render_template('index.html', top_cities=top_cities, least_cities=least_cities,\
                            aqi_population=aqi_population, pollutant=pollutant,\
                            user_date=user_date, comments=comment)


@auth.route('/header')
def header():
    return render_template("header.html")


@auth.route('/login', methods=['GET', 'POST'])
def login_post():
    result = check_login()
    return result


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/newAccount')
def newAccount():
    return render_template("newAccount.html")


@auth.route('/newAccount', methods=['GET', 'POST'])
def newAccount_post():
    email = check_newAccount()
    if email:
        send_notification = email_alert("Account Confirmation", "Thank you for creating an account! We're happy to have you here! Enjoy learning about Air Quality!", email)
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    result = check_logout()
    return result

@auth.route('/accountSetting')
@login_required
def accountSetting():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        curremail = request.form.get('curremail')
        currpass = request.form.get('currpass')
        newpass = request.form.get('newpass')
        confirmpass = request.form.get('confirmpass')
        
        if not firstname or not lastname or not currpass or not newpass or not confirmpass:
            flash('All fields must be filled.')
            return render_template("accountSetting.html")
        
        # Check if the current password is correct
        if not current_user.check_password(currpass):
            flash('Current password is incorrect.')
            return render_template("accountSetting.html")

        # Check if the new password and confirm password match
        if newpass != confirmpass:
            flash('New password and confirm password do not match.')
            return render_template("accountSetting.html")
        
        # Update the user details in the database
        user = User.query.filter_by(email=current_user.email).first()
        user.firstName = firstname
        user.lastName = lastname
        user.password = generate_password_hash(newpass, method='pbkdf2:sha256')

        db.session.commit()

        flash('Account details updated successfully.')
    return render_template("accountSetting.html")


@auth.route('/map', methods=['GET', 'POST'])
@login_required
def map():
    result = perform_map()
    return result


@auth.route('/map_test')
def map_test():
    return render_template('map_test.html')


@auth.route('/latitude', methods=['GET', 'POST'])
def latitude():
    city = request.form.get('city')
    latitude = get_latitude(city)
    return latitude


@auth.route('/longitude', methods=['GET', 'POST'])
def longitude():
    city = request.form.get('city')
    longitude = get_longitude(city)
    return longitude


@auth.route('/analysisMean', methods=['GET', 'POST'])
def analysis_mean():
    city = request.form.get('city')
    mean = get_mean_values(city)
    return mean


@auth.route('/analysisTotal', methods=['GET', 'POST'])
def analysis_total():
    city = request.form.get('city')
    total = get_total_mean(city)
    return total


@auth.route('/analysisPrediction', methods=['GET', 'POST'])
def analysis_prediction():
    city = request.form.get('city')
    data = get_total_mean(city)
    prediction = get_prediction(data)
    prediction_list = prediction.tolist()
    return prediction_list


@auth.route('/testMessage', methods=['GET', 'POST'])
def testMessage():
    recipient = request.form.get('email')
    result = email_alert("Account Confirmation",
                         "Thank you for creating an account! We're happy to have you here! Enjoy learning about Air Quality!",
                         recipient)
    return redirect(url_for('auth.dashboard'))


@auth.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')


@auth.route('/insertComment', methods=['GET', 'POST'])
def insertComment():
    type, result = insert_comment()
    if type == "analysis":
        return redirect(url_for('auth.analysis', city=result))
    else:
        return redirect(url_for('auth.dashboard', date=result))


@auth.route('/analysis', methods=['GET', 'POST'])
def analysis():
    cityName = request.args.get('city')
    result = perform_analysis(cityName)
    return result


@auth.route('/delete_comment', methods=['POST'])
def delete_comment():
    comment_id = request.form.get('commentId')
    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('auth.dashboard'))


@auth.route('/delete_comment_analysis', methods=['POST'])
def delete_comment_analysis():
    comment_id = request.form.get('commentId')
    city = request.form.get('city')
    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('auth.analysis', city=city))
