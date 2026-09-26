import pytest
import requests

# endpoints urls
@pytest.fixture
def base_url():
  return "http://127.0.0.1:8000/api"

@pytest.fixture
def login_url(base_url):
  return f"{base_url}/login"

@pytest.fixture
def employees_url(base_url):
  return f"{base_url}/employees"

# api payloads
@pytest.fixture
def login_payload():
  return {
    'username': 'admin',
    'password': 'admin'
  }

@pytest.fixture
def create_employee_correct_payload():
  return {
    "name": "Batosław",
    "salary": 12_345,
    "age": 30,
    "position": "Junior QA",
    "on_leave": False
  }


# headers for authentication
@pytest.fixture
def auth_headers(login_url, login_payload):
    login_response = requests.post(url=login_url, json=login_payload)
    access_token = login_response.json()['access_token']
    return {
        'Authorization': f'Bearer {access_token}',
    }
