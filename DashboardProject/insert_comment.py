from flask import request
from DashboardProject.models import Comment, City
from DashboardProject import db

""""""
def insert_comment():
    city = request.form.get('city')
    comment = request.form.get('comment')
    city = City.query.filter_by(cityName=city).first()
    new_comment = Comment(pageType="analysis",commentText=comment) #,cityId=city.cityId

    db.session.add(new_comment)
    db.session.commit()

    return 'Comment successfuly added!'
