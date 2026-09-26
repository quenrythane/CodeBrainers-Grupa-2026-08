import requests
import pytest

@pytest.mark.api_test
@pytest.mark.get_employees
def test_get_employees(employees_url, auth_headers):
  # Act
  response = requests.get(url=employees_url, headers=auth_headers)

  # Assert
  response_body = response.json()
  assert response.status_code == 200
