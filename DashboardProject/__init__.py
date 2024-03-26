import csv
from datetime import datetime

from flask import Flask, request, jsonify
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from os import path
import pandas as pd
from sqlalchemy.orm import sessionmaker, relationship

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models import City, Pollutant, User, Comment

    db.init_app(app)
    if not path.exists('bluebuffalo/DashboardProject/' + DB_NAME):
        with app.app_context():
            db.create_all()

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    return app


def create_database(app):
    if not path.exists('bluebuffalo/DashboardProject/' + DB_NAME):
        with app.app_context():
            db.create_all()
            # Read data from CSV and insert into tables
            # insert_data_from_csv()
        print("Created Database!")


# def insert_data_from_csv():
#     from .models import City, Pollutant
#     # Read data from your CSV file (adjust the filename as needed)
#     csv_filename = r'C:\Users\leosc\Documents\GitHub\bluebuffalo\Data\processed\pollution.csv'
#     df = pd.read_csv(csv_filename)

#     # Create SQLAlchemy session
#     Session = sessionmaker(bind=db.engine)
#     session = Session()

#     try:
#         for index, row in df.iterrows():
#             date_obj = datetime.strptime(row['Date'], '%Y-%m-%d')
#             # Create City record
#             city_record = City(cityName=row['City'],
#                                population=row['Population (at 2000)'],
#                                latitude=row['Latitude'],
#                                longitude=row['Longitude'])
#             session.add(city_record)

#             # Create Pollutant record
#             pollutant_record = Pollutant(city=city_record,
#                                          date=date_obj,
#                                          O3Mean=row['O3 Mean'],
#                                          O3AQI=row['O3 AQI'],
#                                          COMean=row['CO Mean'],
#                                          COAQI=row['CO AQI'],
#                                          SO2Mean=row['SO2 Mean'],
#                                          SO2AQI=row['SO2 AQI'],
#                                          NO2Mean=row['NO2 Mean'],
#                                          NO2AQI=row['NO2 AQI'])
#             session.add(pollutant_record)

#         session.commit()
#         print("Data inserted successfully!")
#     except Exception as e:
#         session.rollback()
#         print(f"Error inserting data: {str(e)}")
#     finally:
#         session.close()
