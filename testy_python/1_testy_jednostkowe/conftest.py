import pytest


@pytest.fixture
def employee_fixture():
    employee = {
        "name": "Artur",
        "age": 25,
        "salary": 10_000,
        "position": "Junior QA"
    }
    return employee
