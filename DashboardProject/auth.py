from flask import render_template, request, Blueprint
from DashboardProject.analysis import perform_analysis
from DashboardProject.dashboard import get_top10_data, get_least10_data,\
                                        get_pollutant_data, get_aqi_population
from DashboardProject.map import perform_map
from DashboardProject.insert_comment import insert_comment
from DashboardProject.login import check_login

auth = Blueprint('auth', __name__)

@auth.route('/')
def hello_world():  # put application's code here
    """"""
    return 'Hello World!'

@auth.route('/header')
def header():
    """"""
    return render_template("header.html")
@auth.route('/index')
def index():
    """"""
    return render_template("index.html")
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """"""
    result = check_login()
    return result
@auth.route('/newAccount')
def newAccount():
    """"""
    return render_template("newAccount.html")
@auth.route('/accountSetting')
def accountSetting():
    """"""
    return render_template("accountSetting.html")
@auth.route('/map', methods=['GET', 'POST'])
def map():
    """"""
    result = perform_map()
    return result
@auth.route('/map_test')
def map_test():
    """"""
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

@auth.route('/insertComment', methods=['GET', 'POST'])
def insertComment():
    result = insert_comment()
    # return render_template('index.')
    # return redirect(url_for('auth.analysis', city=result))
    return render_template('index.html')

@auth.route('/analysis', methods=['GET', 'POST'])
def analysis():
    cityName = request.form.get('city')
    result = perform_analysis(cityName)
    return result
@auth.route('/test')
def test():
    """"""
    return render_template('test.html')


@auth.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """"""
    if request.method == 'POST':
        user_date = request.form['date']
        top_cities = get_top10_data(user_date)
        least_cities = get_least10_data(user_date)
        pollutant = get_pollutant_data(user_date)
        aqi_population = get_aqi_population(user_date)
        return render_template('index.html', top_cities=top_cities, \
                               least_cities=least_cities, aqi_population=aqi_population,\
                                  pollutant=pollutant, user_date=user_date)
    else:
        user_date = "2020-01-01"
        top_cities = get_top10_data(user_date)
        least_cities = get_least10_data(user_date)
        pollutant = get_pollutant_data(user_date)
        aqi_population = get_aqi_population(user_date)
        return render_template('index.html', top_cities=top_cities, least_cities=least_cities,\
                                aqi_population=aqi_population, pollutant=pollutant,\
                                  user_date=user_date)
@auth.route('/insertComment', methods=['GET', 'POST'])
def insertComment():
    """"""
    result = insert_comment()
    return render_template('index.html')
