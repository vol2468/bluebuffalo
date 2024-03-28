from flask import Flask, render_template, request
import pandas as pd
import sqlite3

def perform_analysis():
    
    city = request.form.get('city')
    
    # TO FIX
    df = pd.read_csv('/Users/joy/Desktop/COSC310/Project/Data/processed/pollution.csv')

    # Convert the date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # PIE CHART
    filtered_df = df[df['City'] == city]
    
    mean_values = filtered_df[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].mean().values.tolist()


    filtered_df_2000 = df[(df['City'] == city) & (df['Date'] == '2000-01-01')]
    filtered_df_2004 = df[(df['City'] == city) & (df['Date'] == '2004-01-01')]
    filtered_df_2008 = df[(df['City'] == city) & (df['Date'] == '2008-01-01')]
    filtered_df_2012 = df[(df['City'] == city) & (df['Date'] == '2010-01-01')]
    filtered_df_2016 = df[(df['City'] == city) & (df['Date'] == '2014-01-01')]
    filtered_df_2020 = df[(df['City'] == city) & (df['Date'] == '2018-01-01')]
    filtered_df_2021 = df[(df['City'] == city) & (df['Date'] == '2021-01-01')]

    # Time-series
    total_values_list = [
        filtered_df_2000[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2004[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2008[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2012[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2016[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2020[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum(),
        filtered_df_2021[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].values.sum()
    ]

    # MAP FOR TEST
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    
    # ACTUAL CODE
    # latitude, longitude = get_coordinates(city)

    return render_template("analysis.html", meanData=mean_values, city=city, total=total_values_list, lat=latitude, long=longitude)

