# from flask import Flask, render_template, request
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# analysis = Flask(__name__) 
# @analysis.route('/') 

# def analysis():
#     sns.set_theme(style="whitegrid",
#                 font_scale=1.2, # This scales the fonts slightly higher
#                 )
#     # And we're going to remove the top and right axis lines
#     plt.rc("axes.spines", top=False, right=False)

#     df = pd.read_csv('../data/processed/pollution.csv')

#     df['Total AQI'] = df['O3 AQI'] + df['CO AQI'] + df['SO2 AQI'] + df['NO2 AQI']
#     # df.head()

#     city = "Phoenix" #input from user

#     df_filtered = df[df['City'] == city]
#     # df_filtered.head()

#     # Convert the 'date' column to datetime format
#     df_filtered['Date'] = pd.to_datetime(df_filtered['Date'])

#     # Filter the DataFrame to keep only rows where the date is '01-01'
#     newdf_filtered = df_filtered.query("Date.dt.month == 1 and Date.dt.day == 1 and (Year==2000 or Year==2004 or Year==208 or Year==2012 or Year==2016 or Year==2020 or Year==2021)" )

#     date=newdf_filtered['Date']

#     total=newdf_filtered['Total AQI']

#     return render_template('analysis.html', Date=date, Total=total)


# if __name__ == '__main__': 
#     analysis() 
