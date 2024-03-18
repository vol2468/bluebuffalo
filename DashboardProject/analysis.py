from flask import Flask, render_template, request
import json
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
from markupsafe import Markup
import pandas as pd

analysis = Flask(__name__) 
@analysis.route('/analysis.py', methods=['POST']) 


def perform_analysis():
    
    city = request.form.get('city')
    
    # TO FIX
    df = pd.read_csv('/Users/joy/Desktop/COSC310/Project/Data/processed/pollution.csv')

    # Convert the date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    filtered_df = df[df['City'] == city]
    
    mean_values = filtered_df[['O3 Mean', 'CO Mean', 'SO2 Mean', 'NO2 Mean']].mean().values.tolist()

    return render_template("analysis.html", meanData=mean_values, city=city)
