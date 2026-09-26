import requests
import pytest

@pytest.mark.api_login
def test_logowanie():
  base_url = "http://127.0.0.1:8000/api"
  login_url = f"{base_url}/login"

  my_headers = {
    'Content-Type': 'application/json',
  }

  my_payload = {
    "username": "admin",
    "password": "admin"
  }

  response = requests.post(url=login_url, headers=my_headers, json=my_payload)

  response_body = response.json()
  assert response.status_code == 200
  assert 'access_token' in response_body
  assert response_body['token_type'] == 'bearer'
  assert response_body['expires_in'] == 600
