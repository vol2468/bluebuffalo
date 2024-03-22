import csv
from flask import Flask, request, jsonify
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Comment, City, Pollutant

    create_database(app)
    register_csv_upload_route(app)

    return app


def register_csv_upload_route(app):
    @app.route('/upload_csv', methods=['POST'])
    def upload_csv():
        file = request.files['file']
        if not file:
            return jsonify({'error: no file provided'}), 400
        if file.filename.endswith('.csv'):
            try:
                with app.app_context():
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Assuming the CSV structure matches the models
                        city = City(cityName=row['City'],
                                    population=row['Population (at 2000)'],
                                    latitude=row['Latitude'],
                                    longitude=row['Longitude'])
                        db.session.add(city)
                        db.session.commit()

                        # Assuming you have a Pollutant model to store pollutant data
                        pollutant = Pollutant(cityId=city.id,
                                              date=row['Date'],
                                              O3Mean=row['O3 Mean'],
                                              O3AQI=row['O3 AQI'],
                                              COMean=row['CO Mean'],
                                              COAQI=row['CO AQI'],
                                              SO2Mean=row['SO2 Mean'],
                                              SO2AQI=row['SO2 AQI'],
                                              NO2Mean=row['NO2 Mean'],
                                              NO2AQI=row['NO2 AQI'])
                        db.session.add(pollutant)
                        db.session.commit()
            except Exception as e:
                return jsonify({"error": str(e)}), 500

            return jsonify({"message": "CSV data uploaded successfully"}), 200
        else:
            return jsonify({"error": "Invalid file format, only CSV files are accepted"}), 400


def create_database(app):
    if not path.exists('bluebuffalo/DashboardProject/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")