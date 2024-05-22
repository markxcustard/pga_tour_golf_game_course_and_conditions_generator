import pytest
import sqlite3
import os
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
        "DATABASE": "test_golf_course_results.db"  # Use test database
    })

    # Create a temporary database
    with sqlite3.connect(flask_app.config["DATABASE"]) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            course TEXT, crowd TEXT, time_of_day TEXT, tee TEXT, pin TEXT,
                            wind_direction TEXT, wind_speed TEXT, green_firmness TEXT,
                            green_speed TEXT, fringe_firmness TEXT, fringe_speed TEXT,
                            fairway_firmness TEXT, fairway_speed TEXT, first_cut_firmness TEXT,
                            first_cut_length TEXT, second_cut_firmness TEXT, second_cut_length TEXT,
                            timestamp TEXT)''')
        conn.commit()

    yield flask_app

    # Teardown
    if os.path.exists(flask_app.config["DATABASE"]):
        os.remove(flask_app.config["DATABASE"])

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'Golf Course Generator' in response.data

def test_favicon(client):
    response = client.get("/favicon.ico")
    assert response.status_code == 404

def test_generate_course(client):
    response = client.get("/generate_course")
    assert response.status_code == 200
    data = response.get_json()
    assert "course" in data
    assert "timestamp" in data

    # Verify data is inserted into the database
    conn = sqlite3.connect(flask_app.config["DATABASE"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results WHERE timestamp=?", (data['timestamp'],))
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == data['course']  # Verify the course name
    conn.close()

def test_get_results(client):
    response = client.get("/results")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_generate_course_error_handling(client, monkeypatch):
    # Simulate an error during course generation
    def mock_generate_course_info():
        raise Exception("Simulated error")

    monkeypatch.setattr('golf_game.GolfGame.generate_course_info', mock_generate_course_info)

    response = client.get("/generate_course")
    assert response.status_code == 500
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "An error occurred while generating the course."
