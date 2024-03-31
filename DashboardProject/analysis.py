from flask import Flask, render_template, request
import pandas as pd
import sqlite3
from DashboardProject.models import Pollutant, City
from DashboardProject import db
from sqlalchemy import func

# Connection to database
conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

def perform_analysis():
    
    city = request.form.get('city')
    
    # TO FIX
    df = pd.read_csv('/Users/joy/Desktop/COSC310/bluebuffalo/data/processed/pollution.csv')

    # Convert the date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # PIE CHART
    # filtered_df = df[df['City'] == city]
    
    # mean_values = filtered_df[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].mean().values.tolist()

    # # Time-series
    filtered_df_2000 = df[(df['City'] == city) & (df['Date'] == '2000-01-01')]
    filtered_df_2004 = df[(df['City'] == city) & (df['Date'] == '2004-01-01')]
    filtered_df_2008 = df[(df['City'] == city) & (df['Date'] == '2008-01-01')]
    filtered_df_2012 = df[(df['City'] == city) & (df['Date'] == '2012-01-01')]
    filtered_df_2016 = df[(df['City'] == city) & (df['Date'] == '2016-01-01')]
    filtered_df_2020 = df[(df['City'] == city) & (df['Date'] == '2020-01-01')]
    filtered_df_2021 = df[(df['City'] == city) & (df['Date'] == '2021-01-01')]

    total_values_list = [
        filtered_df_2000[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2004[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2008[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2012[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2016[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2020[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2021[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum()
    ]

    
    # ACTUAL CODE
    latitude = get_latitude(city)
    longitude = get_longitude(city)
    mean_values = get_mean_values(city)
    # total_values_list = get_total_mean(city)

    return render_template("analysis.html", meanData=mean_values, city=city, total=total_values_list, lat=latitude, long=longitude)


# Getting corrdinate of specific city from database
def get_latitude(city_name):
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        return city.latitude
    return None

def get_longitude(city_name):
    city = City.query.filter_by(cityName=city_name).first()
    if city:
        return city.longitude
    return None

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