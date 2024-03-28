from DashboardProject.models import Pollutant
from datetime import datetime
from . import app

# Assuming you have a Flask app context (e.g., within a route handler)
with app.app_context():
    # Specify the city ID and date for the query
    city_id = 1  # Replace with the actual city ID
    query_date = datetime.strptime('2000-01-01', '%Y-%m-%d')  # Replace with the actual date

    # Query the Pollutant table
    pollutant_data = Pollutant.query.filter_by(cityId=city_id, date=query_date).first()

    if pollutant_data:
        print(f"Pollutant data for city {city_id} on {query_date}:")
        print(f"O3Mean: {pollutant_data.O3Mean}")
        print(f"O3AQI: {pollutant_data.O3AQI}")
        print(f"COMean: {pollutant_data.COMean}")
        print(f"COAQI: {pollutant_data.COAQI}")
        print(f"SO2Mean: {pollutant_data.SO2Mean}")
        print(f"SO2AQI: {pollutant_data.SO2AQI}")
        print(f"NO2Mean: {pollutant_data.NO2Mean}")
        print(f"NO2AQI: {pollutant_data.NO2AQI}")
    else:
        print(f"No pollutant data found for city {city_id} on {query_date}.")
