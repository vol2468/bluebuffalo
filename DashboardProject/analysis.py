from flask import render_template
import pandas as pd
import sqlite3
from DashboardProject.models import Pollutant, City, Comment
from DashboardProject import db

# Connection to database
conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

def perform_analysis(city):

    # ACTUAL CODE
    latitude = get_latitude(city)
    longitude = get_longitude(city)
    # PIE CHART
    mean_values = get_mean_values(city)
    # Time-series
    total_values_list = get_total_mean(city)
    # Comments
    comments = display_comment(city)
    
    return render_template("analysis.html", meanData=mean_values, city=city, total=total_values_list, lat=latitude, long=longitude, comment = comments)


# Getting corrdinate of specific city from database
def get_latitude(city_name):
    """"""
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        return city.latitude
    return None
def get_longitude(city_name):
    """"""
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        return city.longitude
    return None
# Getting mean value from database
def get_mean_values(city_name):
    """"""
    city = City.query.filter_by(cityName=city_name).first()
    mean_values = db.session.query(
        db.func.avg(Pollutant.O3Mean),
        db.func.avg(Pollutant.COMean),
        db.func.avg(Pollutant.SO2Mean),
        db.func.avg(Pollutant.NO2Mean)
    ).filter_by(cityId=city.cityId).first()
    mean_values_list = [float(value) for value in mean_values]

    return mean_values_list

def get_total_mean(city_name):
    total_values_list=[]
    city = City.query.filter_by(cityName=city_name).first()
    # Query rows from the Pollutant table for the given date range
    for year in range(2000,2022):
        rows = db.session.query(Pollutant) \
                        .filter(Pollutant.date >= f'{year}-01-01', Pollutant.date < f'{year + 1}-01-01') \
                        .filter(Pollutant.cityId == city.cityId) \
                        .all()
        sums = [row.O3Mean + row.COMean + row.SO2Mean + row.NO2Mean for row in rows]
        mean_of_sums = sum(sums) / len(sums) if len(sums) > 0 else 0
        total_values_list.append(mean_of_sums)

    return total_values_list

def display_comment(city_name):
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        comments = Comment.query.filter_by(cityId=city.cityId).all()
        return comments
    return []