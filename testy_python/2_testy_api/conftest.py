import pytest

@pytest.fixture
def base_url():
  return "http://127.0.0.1:8000/api"

@pytest.fixture
def login_url(base_url):
  return f"{base_url}/login"

@pytest.fixture
def login_payload():
  return {
    'username': 'admin',
    'password': 'admin'
  }






@pytest.fixture
def auth_headers():
  return {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
  }
