from DashboardProject.models import Comment
from flask import app, render_template

def test_dashboard(client):
    response = client.get("/")
    assert b"<title>Dashboard</title>" in response.data

# # TO ASK
# def test_analysis(client):
#     response = client.post("/analysis", data={"city": "Phoenix", "latitude": "33.46701848579644", "longitude": "-112.04594469280266"})
#     # Parse the response data as JSON
#     data = response.json

#     meanData = [0.02884219191154196, 0.5274592119054832, 1.4354918684489548, 19.722046015828536]

#     for value in data['meanData']:
#         for mean in meanData:
#             assert value == mean
#     # response = client.get("/analysis.html")

#     # mock_render_template.assert_called_once_with(
#     #         "analysis.html",
#     #         meanData=[0.02884219191154196, 0.5274592119054832, 1.4354918684489548, 19.722046015828536],
#     #         city='Phoenix',
#     #         total=[22.940379, 29.932123, 41.97392000000001, 66.917129, 55.273219000000005, 33.625113999999996, 27.002043999999998],
#     #         lat='33.46701848579644',
#     #         long='-112.04594469280266'
#     #     )

def test_analysiscomment(client, app):
    response = client.post("/insertComment", data={"comment": "It iiiis good.", "city":"Phoenix"})

    with app.app_context():
        assert Comment.query.count() == 4
        assert Comment.query.first().commentText == "It was good."