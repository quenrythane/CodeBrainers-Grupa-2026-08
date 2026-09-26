import requests
import pytest

@pytest.mark.get_employees
def test_get_employees():
  base_url = "http://127.0.0.1:8000/api"
  get_employees_url = f"{base_url}/employees"


  # logowanie do api
  login_url = f"{base_url}/login"

  login_payload = {
    "username": "admin",
    "password": "admin"
  }

  login_response = requests.post(url=login_url, json=login_payload)
  access_token = login_response.json()['access_token']


  # test get employees
  auth_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
  }

  response = requests.get(url=get_employees_url, headers=auth_headers)

  response_body = response.json()
  assert response.status_code == 200
