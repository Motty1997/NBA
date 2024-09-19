from flask import Flask
from controllers.player_controller import players_blueprint  # Replace 'your_module' with the actual module name
import pytest
from repository.database import create_tables, get_db_connection


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(players_blueprint)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_search_user(client):
    response = client.get('/?position=PF&season=2022')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data)>0



# @pytest.fixture(scope="module")
# def setup_database():
#     create_tables()
#     yield
#     # tear down - happens after test finished
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("DROP TABLE players; DROP TABLE dream_teams;")
#     connection.commit()
#     cursor.close()
#     connection.close()

