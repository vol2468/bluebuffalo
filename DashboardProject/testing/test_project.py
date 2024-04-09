from DashboardProject.models import Comment
from unittest.mock import patch
from DashboardProject.message import email_alert
from unittest.mock import Mock
from DashboardProject import create_app


def test_dashboard(client):
    """"""
    response = client.get("/dashboard")
    assert b"<title>Dashboard</title>" in response.data

def test_analysiscomment(client, app):
    """"""
    response = client.post("/insertComment", data={"comment": "It is good.",\
                                                    "city":"Phoenix"})

    with app.app_context():
        assert Comment.query.count() == 0
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
    expected_values = [123.10919540229885,122.95808383233533,108.03048780487805,108.05970149253731,101.06002928257686,93.06666666666666,97.9294670846395,92.84507042253522,88.95287958115183,89.26099290780142,81.70931849791377]
    assert actual_values == expected_values

def test_prediction(client):
    response = client.post("/analysisPrediction", data={"city": "Phoenix"})
    decoded_data = response.data.decode("utf-8")
    print(decoded_data)
    actual_values = [float(value) for value in decoded_data[1:-2].split(',')]
    expected_values = [77.03942314889355, 73.10687408317335, 69.17432501745361, 65.24177595173387, 61.30922688601413]
    assert actual_values == expected_values
def test_email_alert():
    app = create_app()

    with app.app_context():
        # Define test data
        subject = "Test Subject"
        body = "Test Body"
        to = "recipient@example.com"

        with patch('smtplib.SMTP', autospec=True) as mock_smtp_class:

            email_alert(subject, body, to)

            # Assert that the SMTP server was initialized
            mock_smtp_class.assert_called_once_with("smtp.gmail.com", 587)

            # Get the instance of the mock SMTP class
            mock_smtp_instance = mock_smtp_class.return_value

            # Assert that starttls() was called
            mock_smtp_instance.starttls.assert_called_once()

            # Assert that login() was called
            mock_smtp_instance.login.assert_called_once_with("bluebuffalo54321@gmail.com", "chyf iekq vtwy vsbh")

            # Get the actual call arguments for send_message()
            actual_call_args = mock_smtp_instance.send_message.call_args[0]

            # Assert that send_message() was called with the correct parameters
            expected_msg = (
                "Subject: Test Subject\n"
                "To: recipient@example.com\n"
                "From: bluebuffalo54321@gmail.com\n"
                "\n"
                "Test Body"
            )
            actual_email_message = actual_call_args[0].as_string()
            actual_body = actual_email_message.split('\n\n', 1)[1].strip()
            expected_body = expected_msg.split('\n\n', 1)[1].strip()

            # Assert that body match
            assert actual_body == expected_body

            # Assert that quit() was called
            mock_smtp_instance.quit.assert_called_once()