import pytest
from api_client.employees_client import EmployeesAPIClient


@pytest.mark.create_employee_v2
def test_create_employee_v2(base_url, auth_headers, create_employee_correct_payload):
  # Arrange
  employees_api_client = EmployeesAPIClient(base_url)
  employees_api_client.set_auth_headers(auth_headers)

  # Act
  response = employees_api_client.create_employee(create_employee_correct_payload)

  # Assert
  response_body = response.json()
  assert response.status_code == 200
  for key, value in create_employee_correct_payload.items():
    assert response_body[key] == value
  assert 'id' in response_body
  assert isinstance(response_body['id'], int)
