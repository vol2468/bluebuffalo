from DashboardProject.models import Comment

def test_dashboard(client):
    """"""
    response = client.get("/")
    assert b"<title>Dashboard</title>" in response.data

def test_analysiscomment(client, app):
    """"""
    response = client.post("/insertComment", data={"comment": "It is good.",\
                                                    "city":"Phoenix"})

    with app.app_context():
        assert Comment.query.count() == 1
        assert Comment.query.first().commentText == "It is good."
