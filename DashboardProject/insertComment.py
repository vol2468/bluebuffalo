from flask import request, render_template
from DashboardProject.models import Comment, City
from DashboardProject import db


def insert_comment():
    city = request.form.get('city')
    comment = request.form.get('comment')
    cId = City.query.filter_by(cityName=city).first()
    new_comment = Comment(pageType="analysis",commentText=comment,cityId=cId)

    db.session.add(new_comment)
    db.session.commit()

    return 'Comment successfuly added!'