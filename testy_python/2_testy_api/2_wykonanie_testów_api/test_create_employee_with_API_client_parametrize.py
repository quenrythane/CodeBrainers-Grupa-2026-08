import pytest
from api_client.employees_client import EmployeesAPIClient

@pytest.mark.create_employee_v2_parametrize
@pytest.mark.parametrize("employee_data", [
  {
    "name": "Batosław",
    "salary": 12_345,
    "age": 30,
    "position": "Junior QA",
    "on_leave": False
  },
  {
    "name": "Ania",
    "salary": 20_000,
    "age": 25,
    "position": "Senior QA",
    "on_leave": False
  },
  {
    "name": "Karol",
    "salary": 15_000,
    "age": 28,
    "position": "Mid QA",
    "on_leave": False
  }
])
def test_create_employee(base_url, auth_headers, employee_data):
  # Arrange
  employees_api_client = EmployeesAPIClient(base_url)
  employees_api_client.set_auth_headers(auth_headers)

  # Act
  response = employees_api_client.create_employee(employee_data)

  # Assert
  response_body = response.json()
  assert response.status_code == 200
  for key, value in employee_data.items():
    assert response_body[key] == value
  assert 'id' in response_body
  assert isinstance(response_body['id'], int)
