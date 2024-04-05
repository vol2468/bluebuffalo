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
        assert Comment.query.count() == 4
        assert Comment.query.first().commentText == "It was good."

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

def test_total_value(client):
    response = client.post("/analysisTotal", data={"city": "Phoenix"})
    decoded_data = response.data.decode("utf-8")
    print(decoded_data)
    actual_values = [float(value) for value in decoded_data[1:-2].split(',')]
    expected_values = [123.10919540229885,122.95808383233533,108.03048780487805,108.05970149253731,101.06002928257686,93.06666666666666,97.9294670846395,92.84507042253522,88.95287958115183,89.26099290780142,81.70931849791377]
    assert actual_values == expected_values

def test_prediction(client):
    response = client.post("/analysisPrediction", data={"city": "Phoenix"})
    decoded_data = response.data.decode("utf-8")
    print(decoded_data)
    actual_values = [float(value) for value in decoded_data[1:-2].split(',')]
    expected_values = [77.03942314889355, 73.10687408317335, 69.17432501745361, 65.24177595173387, 61.30922688601413]
    assert actual_values == expected_values