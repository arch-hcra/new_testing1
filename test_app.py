import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post("/", data={"username": "admin1", "password": "12345"})
    assert b"Login Yes" in response.data
    assert "Group: admin" in response.data.decode()

def test_login_fail(client):
    response = client.post("/", data={"username": "admin1", "password": "wrongpass"})
    assert b"Login No" in response.data

def test_log_file_written(tmp_path):
    log_file = tmp_path / "login.log"
    global LOG_FILE
    LOG_FILE = str(log_file)


