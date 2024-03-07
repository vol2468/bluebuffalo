from flask import Flask, render_template

map = Flask(__name__)

@map.route("/")
def map():
    return render_template('map.html')

if __name__ == '__main__':
   map.run()