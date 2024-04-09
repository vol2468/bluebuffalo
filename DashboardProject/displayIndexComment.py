from DashboardProject.models import Comment
def display_comment_index(date):
    comments = Comment.query.filter_by(pageType="index", graphDate=date).all()
    if not comments:
        comments = [{"commentText":"Post your comments!"}]
    return comments

