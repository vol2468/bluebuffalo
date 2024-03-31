from DashboardProject.models import Comment
from flask import app, render_template
import json

def test_dashboard(client):
    response = client.get("/")
    assert b"<title>Dashboard</title>" in response.data

def test_analysiscomment(client, app):
    response = client.post("/insertComment", data={"comment": "It is good.", "city":"Phoenix"})

    with app.app_context():
        assert Comment.query.count() == 1
        assert Comment.query.first().commentText == "It is good."

def test_latitude(client):
    response = client.post("/latitude", data={"city": "Phoenix"})
    expected_value = "33.4670184857964"
    assert response.data.decode("utf-8") == expected_value

def test_longitude(client):
    response = client.post("/longitude", data={"city": "Phoenix"})
    expected_value = "-112.045944692803"
    assert response.data.decode("utf-8") == expected_value

def test_mean_value(client):
    response = client.post("/analysisMean", data={"city": "Phoenix"})
    decoded_data = response.data.decode("utf-8")
    actual_values = [float(value) for value in decoded_data[1:-2].split(',')]
    expected_values = [0.02884219191154162, 0.5274592119054846, 1.4354918684489446, 19.722046015828575]
    assert actual_values == expected_values

# def test_total_value(client):

