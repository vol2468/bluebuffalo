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
        assert Comment.query.count() == 3
        assert Comment.query.first().commentText == "It was good."

def test_latitude(client):
    response = client.post("/latitude", data={"city": "Phoenix"})
    expected_value = "33.46701849"
    assert response.data.decode("utf-8") == expected_value

def test_longitude(client):
    response = client.post("/longitude", data={"city": "Phoenix"})
    expected_value = "-112.0459447"
    assert response.data.decode("utf-8") == expected_value

def test_mean_value(client):
    response = client.post("/analysisMean", data={"city": "Phoenix"})
    decoded_data = response.data.decode("utf-8")
    actual_values = [float(value) for value in decoded_data[1:-2].split(',')]
    expected_values = [0.028842191911541974, 0.5274592119054826, 1.4354918684489522, 19.722046015828546]
    assert actual_values == expected_values

def test_total_value(client):
    response = client.post("/analysisTotal", data={"city": "Phoenix"})
    decoded_data = response.data.decode("utf-8")
    print(decoded_data)
    actual_values = [float(value) for value in decoded_data[1:-2].split(',')]
    expected_values = [32.46216454597701, 32.225712304469276, 33.64506884730539, 32.68671943624161, 27.4499418597561, 27.0385659543379, 25.09386622814499, 24.8737923005698, 23.399155619326503, 21.773384290322582, 20.159117142424243, 21.471525112570355, 21.634196951410658, 19.588986527687297, 19.727166454929577, 16.7573741911315, 17.107009959860385, 19.26763898679868, 17.18575670496454, 15.297335178370787, 15.556277061196107, 12.92152160557769]
    assert actual_values == expected_values
