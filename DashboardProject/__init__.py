from datetime import datetime
from os import path
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
from .views import views
from .auth import auth
from .models import City, Pollutant
from sqlalchemy.exc import SQLAlchemyError


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    """"""  
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    if not path.exists('bluebuffalo/DashboardProject/' + DB_NAME):
        with app.app_context():
            db.create_all()

    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #create_database(app)

    return app

def create_database(app):
    """"""
    if not path.exists('bluebuffalo/DashboardProject/' + DB_NAME):
        with app.app_context():
            db.create_all()
            # Read data from CSV and insert into tables
            insert_data_from_csv()
        print("Created Database!")
        # Call the method to execute the script
        delete_duplicates_and_reset_ids()

def insert_data_from_csv():
    """"""
    # Read data from your CSV file (adjust the filename as needed)
    csv_filename = r'/Users/joy/Desktop/COSC310/bluebuffalo/data/processed/pollution.csv'

    df = pd.read_csv(csv_filename)

    # Create SQLAlchemy session
    session_maker = sessionmaker(bind=db.engine)
    session = session_maker()

    try:
        for row in df.iterrows():
            # Create City record if it doesn't exist
            city = City.query.filter_by(cityName=row['City']).first()
            if not city:
                city = City(cityName=row['City'],
                            population=row['Population (at 2000)'],
                            latitude=row['Latitude'],
                            longitude=row['Longitude'])
                session.add(city)
                session.commit()
            city_id = city.cityId

            date_obj = datetime.strptime(row['Date'], '%Y-%m-%d')
            # Create Pollutant record
            pollutant_record = Pollutant(
                cityId=city_id,
                date=date_obj,
                O3Mean=row['O3 Mean'],
                O3AQI=row['O3 AQI'],
                COMean=row['CO Mean'],
                COAQI=row['CO AQI'],
                SO2Mean=row['SO2 Mean'],
                SO2AQI=row['SO2 AQI'],
                NO2Mean=row['NO2 Mean'],
                NO2AQI=row['NO2 AQI']
            )
            session.add(pollutant_record)
        session.commit()
        print("Data inserted successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting data: {str(e)}")
    finally:
        session.close()
def delete_duplicates_and_reset_ids():
    """"""
    # Establish connection to the database
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()

    try:
        # Create a temporary table to store distinct cities
        cursor.execute("""
        CREATE TEMP TABLE temp_city AS
        SELECT DISTINCT cityName, population, latitude, longitude
        FROM city
        """)

        # Delete all rows from the original city table
        cursor.execute("DELETE FROM city")

        # Copy distinct city records from the temporary table back into the original table
        cursor.execute("""
        INSERT INTO city (cityName, population, latitude, longitude)
        SELECT cityName, population, latitude, longitude
        FROM temp_city
        """)

        # Drop the temporary table
        cursor.execute("DROP TABLE temp_city")

        # Commit changes
        conn.commit()
        print("Duplicate cities deleted and cityId reset successfully.")
    except sqlite3.Error as e:
        # Rollback changes if there's an error
        conn.rollback()
        print("Error:", e)
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()
