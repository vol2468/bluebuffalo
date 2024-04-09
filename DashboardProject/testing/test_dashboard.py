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
            (76, 'Presque Isle', 32),
            (81, 'Boston', 34),
            (97, 'Londonderry', 34),
            (77, 'Portland', 35),
            (174, 'rural Laramie', 35),
            (34, 'Capitan', 36),
            (57, 'rural Ada', 37),
            (101, 'New York', 37),
            (79, 'Grantsville', 39)
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
    assert result[0] == (9, 'Bethel Island', 31)
    assert result[1] == (76, 'Presque Isle', 32)
    assert result[2] == (81, 'Boston', 34)
    assert result[3] == (97, 'Londonderry', 34)
    assert result[4] == (77, 'Portland', 35)
    assert result[5] == (174, 'rural Laramie', 35)
    assert result[6] == (34, 'Capitan', 36)
    assert result[7] == (57, 'rural Ada', 37)
    assert result[8] == (101, 'New York', 37)
    assert result[9] == (79, 'Grantsville', 39)


def test_get_least10_data(mock_db_session):
    # Open an application context
    app = create_app()
    with app.app_context():
        # Mock data for the query result
        mock_query_result = [
            (22, 'Los Angeles', 335),  # (city_id, city_name, total_aqi)
            (25, 'Rubidoux', 280),
            (159, 'Salt Lake City', 238),
            (45, 'Denver', 172),
            (3, 'Phoenix', 153),
            (92, 'St. Louis', 116),
            (44, 'Welby', 95),
            (111, 'Cleveland', 86),
            (1, 'Birmingham', 82),
            (94, 'Sunrise Manor', 80)
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
    assert result[0] == (22, 'Los Angeles', 335)
    assert result[1] == (25, 'Rubidoux', 280)
    assert result[2] == (159, 'Salt Lake City', 238)
    assert result[3] == (45, 'Denver', 172)
    assert result[4] == (3, 'Phoenix', 153)
    assert result[5] == (92, 'St. Louis', 116)
    assert result[6] == (44, 'Welby', 95)
    assert result[7] == (111, 'Cleveland', 86)
    assert result[8] == (1, 'Birmingham', 82)
    assert result[9] == (94, 'Sunrise Manor', 80)


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
    assert result[15] == ('Essex', '39,078', 16.5)
    assert result[16] == ('Deer Park', '28,520', 16.5)
    assert result[17] == ('Kansas City', '146,866', 16.25)
    assert result[18] == ('Philadelphia', '1,517,550', 16.0)
    assert result[19] == ('North Little Rock', '60,433', 15.75)
    assert result[20] == ('Camden', '79,904', 15.75)
    assert result[21] == ('Houston', '1,953,631', 15.5)
    assert result[22] == ('Charlotte', '540,828', 15.25)
    assert result[23] == ('Wilmington', '72,664', 15.0)
    assert result[24] == ('rural DeKalb', 0, 15.0)
    assert result[25] == ('Newark', '273,546', 15.0)
    assert result[26] == ('Salt Lake City', '181,743', 14.875)
    assert result[27] == ('Beltsville', '15,690', 14.75)
    assert result[28] == ('St. Louis', '348,189', 14.5)
    assert result[29] == ('San Jose', '894,943', 14.25)


def test_get_pollutant_data(mock_db_session):
    # Open an application context
    app = create_app()
    with app.app_context():
        # Mock data for the query result
        mock_query_result = [
            (0.0241989493670886),
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
    assert result[0] == (0.0241989493670886)
    assert result[1] == (0.29102832911392396)
    assert result[2] == (0.5780351772151899)
    assert result[3] == (10.794540101265822)