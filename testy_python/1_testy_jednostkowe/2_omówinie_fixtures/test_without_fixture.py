def test_name_employee():
    employee = {
        "name": "Artur",
        "age": 25,
        "salary": 10_000,
        "position": "Junior QA"
    }
    assert employee["name"] == "Artur"


def test_age_employee():
    employee = {
        "name": "Artur",
        "age": 25,
        "salary": 10_000,
        "position": "Junior QA"
    }
    assert employee["age"] == 25
