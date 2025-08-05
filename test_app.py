import pytest
<<<<<<< HEAD
from app_bd import app
=======
from app import app

>>>>>>> 1d01826091ea83b6ccd87d93f60857f4f7b17414

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

<<<<<<< HEAD
def test_login_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter the system" in response.data

def test_login_success(client):
    response = client.post("/", data={"username": "admin1", "password": "12345"})
    assert response.status_code == 200
    assert b"Login Yes" in response.data

def test_login_failure_wrong_password(client):
    response = client.post("/", data={"username": "admin1", "password": "wrong"})
    assert response.status_code == 200
    assert b"Login No" in response.data

def test_login_failure_unknown_user(client):
    response = client.post("/", data={"username": "unknown", "password": "123"})
    assert response.status_code == 200
    assert b"Login No" in response.data

def test_empty_username_password(client):
    response = client.post("/", data={"username": "", "password": ""})
    assert response.status_code == 200
    assert b"Login No" in response.data
=======
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


>>>>>>> 1d01826091ea83b6ccd87d93f60857f4f7b17414
