from pages.manage_employees_page import ManageEmployeesPage
import pytest

@pytest.mark.dodaj_pracownika
@pytest.mark.test_ui
def test_dodaj_pracownika(driver, employee_data, logowanie_ui, wait):
    # Arrange
    ed = employee_data
    manage_employees_page = ManageEmployeesPage(driver, wait)


    # Act
    manage_employees_page.fill_name(ed["name"])
    manage_employees_page.fill_salary(ed["salary"])
    manage_employees_page.fill_age(ed["age"])
    manage_employees_page.fill_position(ed["position"])
    manage_employees_page.fill_on_leave(ed["on_leave"])
    manage_employees_page.submit_form()

    # Assert
    dane_ostatniego_wiersza = manage_employees_page.get_last_employee_data()

    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == ed["name"]
    assert dane_ostatniego_wiersza[2] == str(ed["salary"])
    assert dane_ostatniego_wiersza[3] == str(ed["age"])
    assert dane_ostatniego_wiersza[4] == ed["position"]
    assert dane_ostatniego_wiersza[5] == ("✅" if ed["on_leave"] else "❌")



