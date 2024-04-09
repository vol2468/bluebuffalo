import pytest
from unittest.mock import Mock
from DashboardProject.dashboard import get_top10_data, get_least10_data, get_aqi_population, get_pollutant_data
from DashboardProject import create_app

@pytest.fixture
def mock_db_session():
    # Create a mock database session
    return Mock()

def test_get_top10_data(mock_db_session):
    # Open an application context
    app = create_app()
    with app.app_context():
        # Mock data for the query result
        mock_query_result = [
            (9, 'Bethel Island', 31),
            (96, 'Presque Isle', 64),
            (82, 'Boston', 68),
            (139, 'Londonderry', 68),
            (109, 'Portland', 70),
            (22, 'Capitan', 72),
            (49, 'New York', 74),
            (130, 'East Providence', 78),
            (138, 'Grantsville', 78),
            (145, 'Rutland', 78)
        ]

        # Mock the return value of the query method
        mock_db_session.query.return_value\
                        .join.return_value\
                        .filter.return_value\
                        .group_by.return_value\
                        .order_by.return_value\
                        .limit.return_value\
                        .all.return_value = mock_query_result

        # Call the function with the mock session
        result = get_top10_data('2020-01-01')

    # Assertions
    assert len(result) == 10  # Check if the result contains 10 items
    assert result[0] == (5, 'Bethel Island', 62)
    assert result[1] == (96, 'Presque Isle', 64)
    assert result[2] == (82, 'Boston', 68)
    assert result[3] == (139, 'Londonderry', 68)
    assert result[4] == (109, 'Portland', 70)
    assert result[5] == (22, 'Capitan', 72)
    assert result[6] == (49, 'New York', 74)
    assert result[7] == (130, 'East Providence', 78)
    assert result[8] == (138, 'Grantsville', 78)
    assert result[9] == (145, 'Rutland', 78)


def test_get_least10_data(mock_db_session):
    # Open an application context
    app = create_app()
    with app.app_context():
        # Mock data for the query result
        mock_query_result = [
            (22, 'Los Angeles', 335),  # (city_id, city_name, total_aqi)
            (15, 'Rubidoux', 560),
            (132, 'Salt Lake City', 476),
            (16, 'Not in a city', 346),
            (91, 'Denver', 344),
            (1, 'Phoenix', 306),
            (47, 'St. Louis', 232),
            (28, 'Welby', 190),
            (127, 'Cleveland', 172),
            (135, 'Birmingham', 164)
        ]

        # Mock the return value of the query method
        mock_db_session.query.return_value\
                        .join.return_value\
                        .filter.return_value\
                        .group_by.return_value\
                        .order_by.return_value\
                        .limit.return_value\
                        .all.return_value = mock_query_result

        # Call the function with the mock session
        result = get_least10_data('2020-01-01')

    # Assertions
    assert len(result) == 10  # Check if the result contains 10 items
    assert result[0] == (11, 'Los Angeles', 670)
    assert result[1] == (15, 'Rubidoux', 560)
    assert result[2] == (132, 'Salt Lake City', 476)
    assert result[3] == (16, 'Not in a city', 346)
    assert result[4] == (91, 'Denver', 344)
    assert result[5] == (1, 'Phoenix', 306)
    assert result[6] == (47, 'St. Louis', 232)
    assert result[7] == (28, 'Welby', 190)
    assert result[8] == (127, 'Cleveland', 172)
    assert result[9] == (135, 'Birmingham', 164)


def test_get_aqi_population(mock_db_session):
    # Open an application context
    app = create_app()
    with app.app_context():
        # Mock data for the query result
        mock_query_result = [
            (0.024198949367088607),
            (0.29102832911392407),
            (0.57803517721519),
            (10.794540101265829),
        ]

        # Mock the return value of the query method
        mock_db_session.query.return_value\
                    .join.return_value\
                    .filter.return_value\
                    .group_by.return_value\
                    .order_by.return_value\
                    .limit.return_value\
                    .all.return_value = mock_query_result

        # Call the function with the mock session
        result = get_aqi_population('2020-01-01')

    # Assertions
    assert len(result) == 30  # Check if the result contains 4 items
    assert result[0] == ('Welby', '12,973', 23.75)
    assert result[1] == ('Denver', '554,636', 21.5)
    assert result[2] == ('Birmingham', '242,820', 20.5)
    assert result[3] == ('Sunrise Manor', '156,120', 20.0)
    assert result[4] == ('Washington', '572,059', 19.25)
    assert result[5] == ('Phoenix', '1,321,045', 19.125)
    assert result[6] == ('Reno', '180,480', 19.0)
    assert result[7] == ('Calexico', '27,408', 18.5)
    assert result[8] == ('Victorville', '64,029', 18.0)
    assert result[9] == ('Baton Rouge', '227,818', 18.0)
    assert result[11] == ('Rubidoux', '29,180', 17.5)
    assert result[12] == ('Fontana', '128,929', 17.25)
    assert result[13] == ('Los Angeles', '3,694,820', 16.75)
    assert result[14] == ('El Cajon', '94,869', 16.5)
    assert result[15] == ('Deer Park', '28,520', 16.5)
    assert result[16] == ('El Cajon', '94,869', 16.5)
    assert result[17] == ('Kansas City', '146,866', 16.25)
    assert result[18] == ('Philadelphia', '1,517,550', 16.0)
    assert result[19] == ('Camden', '79,904', 15.75)
    assert result[20] == ('North Little Rock', '60,433', 15.75)
    assert result[21] == ('Houston', '1,953,631', 15.5)
    assert result[22] == ('Charlotte', '540,828', 15.25)
    assert result[23] == ('Newark', '273,546', 15.0)
    assert result[24] == ('Wilmington', '72,664', 15.0)
    assert result[25] == ('Salt Lake City', '181,743', 14.875)
    assert result[26] == ('Beltsville', '15,690', 14.75)
    assert result[27] == ('St. Louis', '348,189', 14.5)
    assert result[28] == ('San Jose', '894,943', 14.25)
    assert result[29] == ('Tucson', '486,699', 14.0)


def test_get_pollutant_data(mock_db_session):
    # Open an application context
    app = create_app()
    with app.app_context():
        # Mock data for the query result
        mock_query_result = [
            (0.024198949367088607),
            (0.29102832911392407),
            (0.57803517721519),
            (10.794540101265829),
        ]

        # Mock the return value of the query method
        mock_db_session.query.return_value\
                    .filter.return_value\
                    .one.return_value = mock_query_result

        # Call the function with the mock session
        result = get_pollutant_data('2020-01-01')

    # Assertions
    assert len(result) == 4  # Check if the result contains 4 items
    assert result[0] == (0.024198949367088607)
    assert result[1] == (0.29102832911392407)
    assert result[2] == (0.57803517721519)
    assert result[3] == (10.794540101265829)