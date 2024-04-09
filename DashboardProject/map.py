from flask import Flask, render_template, json, jsonify
import sqlite3

map = Flask(__name__)

@map.route('/')
def perform_map():
    conn = sqlite3.connect('instance/database.db', check_same_thread=False)
    cursor = conn.cursor()
    try:
        cityList = get_coordinate(cursor)
        return render_template('map.html', cityList=json.dumps(cityList))
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

def get_coordinate(cursor):
    cursor.execute("SELECT cityId, cityName, latitude, longitude FROM city")
    row = cursor.fetchall()
    cityList = []
    for x in range(len(row)):
        for y in range(4):
            cityList.append(row[x][y])
        cityId = row[x][0]
        cityAQI = getAQI(cityId, cursor)
        cityList.append(cityAQI)
    return cityList

def getAQI(cityId, cursor):
    cursor.execute("SELECT AVG(O3AQI) as O3AQI, AVG(COAQI) as COAQI, AVG(SO2AQI) as SO2AQI, AVG(NO2AQI) as NO2AQI FROM pollutant WHERE cityId =? GROUP BY cityId", (cityId,))
    row = cursor.fetchone()
    if row:
        cityAQI = int(row[0]) + int(row[1]) + int(row[2]) + int(row[3])
        return cityAQI
    return None

if __name__ == '__main__':
   map.run()