from datetime import datetime
from flask import Flask
from DashboardProject import db
from DashboardProject.models import Comment
from DashboardProject import create_app
app = create_app()


def test_delete_comment(client):
    with app.app_context():
        # Insert a comment
        comment = Comment(pageType="index", commentText="Test comment", commentDate=datetime.now(), userId=1)
        db.session.add(comment)
        db.session.commit()

        # Delete the comment
        response = client.post('/delete_comment', data={'commentId': comment.commentId})

        expected_status = 302
        # Check the response
        assert response.status_code == expected_status
        # # Check the response

        # Check if the comment is deleted
        comment = Comment.query.filter_by(commentId=comment.commentId).first()
        assert comment is None
