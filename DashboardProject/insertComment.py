from flask import request
from DashboardProject.models import Comment, City
from DashboardProject import db
from datetime import datetime
from datetime import datetime

""""""
def insert_comment():
    city_name = request.form.get('city')
    comment = request.form.get('comment')
    type = request.form.get('pageType')
    date = request.form.get('date')
    city = City.query.filter_by(cityName=city_name).first()
    graph_date = datetime.strptime(date, '%Y-%m-%d')

    if type == "analysis":
        new_comment = Comment(pageType="analysis",commentText=comment,commentDate=datetime.now(),cityId=city.cityId, userId=1) 
    else:
        new_comment = Comment(pageType="index",commentText=comment,commentDate=datetime.now(),graphDate=graph_date,userId=1) 

    db.session.add(new_comment)
    db.session.commit()

    return city_name


