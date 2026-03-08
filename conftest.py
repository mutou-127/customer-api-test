import pytest
import requests

@pytest.fixture
def login_session():
    ses = requests.Session()
    login_url = "http://127.0.0.1/api/mgr/signin"
    login_data = {"username": "byhy", "password": "88888888"}
    ses.post(login_url, data=login_data)
    return ses

