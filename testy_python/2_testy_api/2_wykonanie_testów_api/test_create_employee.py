import requests
import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.api_test
@pytest.mark.create_employee
def test_create_employee(employees_url, auth_headers, create_employee_correct_payload):
  # Act
  logger.debug(f"URL: {employees_url}")
  logger.debug(f"Auth headers: {auth_headers}")
  logger.debug(f"Payload: {create_employee_correct_payload}")
  logger.info("Wysyłanie zapytania POST...")
  response = requests.post(
    url=employees_url,
    headers=auth_headers,
    json=create_employee_correct_payload
  )

  # Assert
  response_body = response.json()
  logger.debug(f"Response: {response_body}")

  assert response.status_code == 200
  for key, value in create_employee_correct_payload.items():
    logger.info(f"Sprawdzam klucz body_response: {key.upper()} o wartości: {str(response_body[key]).upper()}, który powinien mieć wartość {str(value).upper()}")
    assert response_body[key] == value
  assert 'id' in response_body
  logger.info(f"Nowo utworzony pracownik ma ID: {response_body['id']}")
  assert isinstance(response_body['id'], int)
  logger.info(f"Typ ID jest typu {type(response_body['id'])}")

