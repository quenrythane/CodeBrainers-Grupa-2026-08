import requests
import pytest

@pytest.mark.api_login
def test_logowanie(login_url, login_payload):
  # Act
  response = requests.post(url=login_url, json=login_payload)

  # Assert
  response_body = response.json()
  assert response.status_code == 200
  assert 'access_token' in response_body
  assert response_body['token_type'] == 'bearer'
  assert response_body['expires_in'] == 600
