import unittest
from datetime import datetime
from flask import Flask
from DashboardProject import db
from DashboardProject.models import Comment

class DeleteCommentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Use the production database
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        db.init_app(self.app)

    def test_delete_comment(self):
        with self.app.app_context():
            # Insert a comment
            comment = Comment(pageType="index", commentText="Test comment", commentDate=datetime.now(), userId=1)
            db.session.add(comment)
            db.session.commit()

            # Delete the comment
            response = self.client.post('/delete_comment', data={'commentId': comment.commentId})

            # Check the response
            self.assertEqual(response.status_code, 302)  # 302 status code means redirection happened which is expected

            # Check if the comment is deleted
            comment = Comment.query.get(comment.commentId)
            self.assertIsNone(comment)

if __name__ == '__main__':
    unittest.main()
