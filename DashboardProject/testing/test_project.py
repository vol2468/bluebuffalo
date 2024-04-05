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
    expected_values = [123.10919540229885, 115.3659217877095, 122.95808383233533, 116.05369127516778, 108.03048780487805, 108.94292237442923, 108.05970149253731, 101.07977207977208, 101.06002928257686, 94.5750350631136, 93.06666666666666, 92.67729831144466, 97.9294670846395, 92.7442996742671, 92.84507042253522, 89.16207951070336, 88.95287958115183, 93.93399339933994, 89.26099290780142, 84.36938202247191, 81.70931849791377, 94.21115537848605]
    assert actual_values == expected_values
