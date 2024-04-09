from flask import request
from DashboardProject.models import Comment, City
from DashboardProject import db
from datetime import datetime
from datetime import datetime

""""""
def insert_comment():
    city_name = request.args.get('city')
    comment = request.args.get('comment')
    type = request.args.get('pageType')
    date = request.args.get('date')
    city = City.query.filter_by(cityName=city_name).first()


    if type == "analysis":
        new_comment = Comment(pageType="analysis",commentText=comment,commentDate=datetime.now(),cityId=city.cityId, userId=1) 
    else:
        graph_date = datetime.strptime(date, '%Y-%m-%d')
        new_comment = Comment(pageType="index",commentText=comment,commentDate=datetime.now(),graphDate=graph_date,userId=1) 

    db.session.add(new_comment)
    db.session.commit()
    if type == "analysis":
        return type,city_name
    else:
        return type, date



