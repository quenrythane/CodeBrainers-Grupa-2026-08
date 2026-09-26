import requests
import pytest


@pytest.mark.create_employee
def test_create_employee(employees_url, auth_headers, create_employee_correct_payload):
  # Act
  response = requests.post(
    url=employees_url,
    headers=auth_headers,
    json=create_employee_correct_payload
  )

  # Assert
  response_body = response.json()
  assert response.status_code == 200
  for key, value in create_employee_correct_payload.items():
    assert response_body[key] == value
  assert 'id' in response_body
  assert isinstance(response_body['id'], int)
