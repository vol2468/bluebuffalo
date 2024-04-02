from flask import request
from DashboardProject.models import Comment, City
from DashboardProject import db
from datetime import datetime

""""""
def insert_comment():
    city_name = request.form.get('city')
    comment = request.form.get('comment')
    city = City.query.filter_by(cityName=city_name).first()
    commentDate = datetime.now()
    new_comment = Comment(pageType="analysis",commentText=comment,commentDate=commentDate,cityId=city.cityId, userId=1) 

    db.session.add(new_comment)
    db.session.commit()

    return city_name


