import sqlite3
from flask import render_template, request
from DashboardProject.models import Pollutant, City
from DashboardProject import db


# Connection to database
conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()
""""""
def perform_analysis():
    city = request.form.get('city')
    # ACTUAL CODE
    latitude = get_latitude(city)
    longitude = get_longitude(city)
    # PIE CHART
    mean_values = get_mean_values(city)
    # Time-series
    total_values_list = get_total_mean(city)

    return render_template("analysis.html", meanData=mean_values,\
                            city=city, total=total_values_list, \
                                lat=latitude, long=longitude)

""""""
# Getting corrdinate of specific city from database
def get_latitude(city_name):
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        return city.latitude
    return None
""""""
def get_longitude(city_name):
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        return city.longitude
    return None
""""""
# Getting mean value from database
def get_mean_values(city_name):
    city = City.query.filter_by(cityName=city_name).first()
    mean_values = db.session.query(
        db.func.avg(Pollutant.O3Mean),
        db.func.avg(Pollutant.COMean),
        db.func.avg(Pollutant.SO2Mean),
        db.func.avg(Pollutant.NO2Mean)
    ).filter_by(cityId=city.cityId).first()
    mean_values_list = [float(value) for value in mean_values]

    return mean_values_list
""""""
# Getting total values of pollutant in each year from database
def get_total_mean(city_name):
    total_values_list = []
    city = City.query.filter_by(cityName=city_name).first()
    for year in ['2000', '2004', '2008', '2012', '2016', '2020', '2021']:
        total_sum = db.session.query(Pollutant.O3Mean, Pollutant.COMean,\
                                      Pollutant.SO2Mean, Pollutant.NO2Mean) \
                        .filter_by(cityId=city.cityId, date=f'{year}-01-01').first()
        if total_sum is None:
            # Set total_sum to a tuple of zeros
            total_sum = (0, 0, 0, 0)

        total_sum = tuple(map(lambda x: x or 0, total_sum))
        total_values_list.append(sum(total_sum))
    return total_values_list
