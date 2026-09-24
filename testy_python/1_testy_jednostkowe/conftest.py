import pytest
import logging

@pytest.fixture
def employee_fixture():
    employee = {
        "name": "Artur",
        "age": 25,
        "salary": 10_000,
        "position": "Junior QA"
    }
    return employee

@pytest.fixture
def imie():
    return "Michal"

# @pytest.fixture(scope="session", autouse=True)
# def start_sesji_testowej():
#     print("\nRozpoczynam testy")
#     print("\nprzygotowanie danych")
#     yield
#     print("\nKoniec testów")
#     print("\nczyszczenie po testach")

# @pytest.fixture(scope="function", autouse=True)
# def start_testu():
#     print("\nRozpoczynam testy".upper())





