from flask import Flask, render_template, request
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import pandas as pd

analysis = Flask(__name__) 
@analysis.route('/analysis.py', methods=['POST']) 


def perform_analysis():
    
    city = request.form.get('city')
    
    # TO FIX
    df = pd.read_csv('/Users/joy/Desktop/COSC310/Project/Data/processed/pollution.csv')

    # Convert the date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

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
    return render_template("analysis.html", city=city, total=total_values_list)
