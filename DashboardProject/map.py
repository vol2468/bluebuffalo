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
    address = ""
    cityList = get_coordinate()
    return render_template('map.html', cityList=json.dumps(cityList))

def get_coordinate():
    cursor.execute("SELECT cityId, cityName, latitude, longitude FROM city")
    row = cursor.fetchall()
    cityList = []
    for x in range(len(row)):
        for y in range(4):
            cityList.append(row[x][y])
    return cityList

if __name__ == '__main__':
   map.run()