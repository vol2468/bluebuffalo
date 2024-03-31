from DashboardProject import db
from DashboardProject.models import Pollutant, City
from sqlalchemy import func

def get_top10_data(user_date):
    # Retrieve top 10 cities by total AQI for the given date.
    # Query to join pollutant and city tables, calculate total AQI, and group by city
    query = db.session.query(City.cityId, City.cityName, func.sum(Pollutant.O3AQI + Pollutant.COAQI + Pollutant.SO2AQI + Pollutant.NO2AQI).label('totalAQI'))\
                        .join(Pollutant, City.cityId == Pollutant.cityId)\
                        .filter(Pollutant.date == user_date)\
                        .group_by(City.cityId, City.cityName)\
                        .order_by(func.sum(Pollutant.O3AQI + Pollutant.COAQI + Pollutant.SO2AQI + Pollutant.NO2AQI).desc())\
                        .limit(10)\
                        .all()
    return query


def get_least10_data(user_date):
    # Retrieve least 10 cities by total AQI for the given date.
    # Query to join pollutant and city tables, calculate total AQI, and group by city
    query = db.session.query(City.cityId, City.cityName, func.sum(Pollutant.O3AQI + Pollutant.COAQI + Pollutant.SO2AQI + Pollutant.NO2AQI).label('totalAQI'))\
                        .join(Pollutant, City.cityId == Pollutant.cityId)\
                        .filter(Pollutant.date == user_date)\
                        .group_by(City.cityId, City.cityName)\
                        .order_by(func.sum(Pollutant.O3AQI + Pollutant.COAQI + Pollutant.SO2AQI + Pollutant.NO2AQI).asc())\
                        .limit(10)\
                        .all()
    return query


def get_pollutant_data(user_date):
    # Retrieve pollutant ratio for the given date.
    # Query to calculate mean values of pollutants across all cities on the given date
    query = db.session.query(
                        func.avg(Pollutant.O3Mean).label('avgO3Mean'),
                        func.avg(Pollutant.COMean).label('avgCOMean'),
                        func.avg(Pollutant.SO2Mean).label('avgSO2Mean'),
                        func.avg(Pollutant.NO2Mean).label('avgNO2Mean'))\
                        .filter(Pollutant.date == user_date)\
                        .one()
    return query


def get_aqi_population(user_date):
    # Retrieve population and mean AQI for the given date.
    # Query to join pollutant and city tables, calculate mean AQI, and group by city
    query = db.session.query(City.cityName, City.population, func.avg((Pollutant.O3AQI + Pollutant.COAQI + Pollutant.SO2AQI + Pollutant.NO2AQI) / 4).label('meanAQI'))\
                        .join(Pollutant, City.cityId == Pollutant.cityId)\
                        .filter(Pollutant.date == user_date)\
                        .group_by(City.cityId, City.cityName)\
                        .order_by(func.avg((Pollutant.O3AQI + Pollutant.COAQI + Pollutant.SO2AQI + Pollutant.NO2AQI) / 4).desc())\
                        .limit(30)\
                        .all()
    return query