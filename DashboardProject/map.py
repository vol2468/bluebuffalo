from flask import Flask, render_template, request, json
import jinja2
import pandas as pd
import sqlite3

# Connection to database
# conn = sqlite3.connect('../../instance/database.db', check_same_thread=False)     # for testing
conn = sqlite3.connect('instance/database.db', check_same_thread=False)
cursor = conn.cursor()
map = Flask(__name__)
@map.route('/')
def perform_map():
    cityList = get_coordinate()
    return render_template('map.html', cityList=json.dumps(cityList))

def get_coordinate():
    cursor.execute("SELECT cityId, cityName, latitude, longitude FROM city")
    row = cursor.fetchall()
    cityList = []
    for x in range(len(row)):
        for y in range(4):
            cityList.append(row[x][y])
        cityId = row[x][0]
        cityAQI = getAQI(cityId)
        cityList.append(cityAQI)
    return cityList

def getAQI(cityId):
    cursor.execute("SELECT AVG(O3AQI) as O3AQI, AVG(COAQI) as COAQI, AVG(SO2AQI) as SO2AQI, AVG(NO2AQI) as NO2AQI FROM pollutant WHERE cityId =? GROUP BY cityId", (cityId,))
    row = cursor.fetchone()
    if row:
        cityAQI = int(row[0]) + int(row[1]) + int(row[2]) + int(row[3])
        return cityAQI
    return None

if __name__ == '__main__':
   map.run()