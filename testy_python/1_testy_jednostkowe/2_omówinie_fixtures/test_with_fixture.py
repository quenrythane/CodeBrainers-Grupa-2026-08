# pobieramy fixture z pliku conftest.py
def test_name_employee(employee_fixture):
    assert employee_fixture["name"] == "Artur"


def test_age_employee(employee_fixture):
    assert employee_fixture["age"] == 25
