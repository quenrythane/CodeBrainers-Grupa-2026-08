import pytest
from pages.employee_manager_page import EmployeeManagerPage

@pytest.mark.dodaj_pracownika
@pytest.mark.test_ui
def test_dodaj_pracownika(driver, employee_data, logowanie_ui, wait):
    ed = employee_data
    emp_page = EmployeeManagerPage(driver, wait)

    # Act
    emp_page.fill_name_input(ed["name"])
    emp_page.fill_salary_input(ed["salary"])
    emp_page.fill_age_input(ed["age"])
    emp_page.select_position_select(ed["position"])
    emp_page.click_on_vacation_checkbox(ed["on_leave"])
    emp_page.click_add_btn()


    # Assert
    dane_ostatniego_wiersza = emp_page.get_data_from_last_row()

    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == ed["name"]
    assert dane_ostatniego_wiersza[2] == str(ed["salary"])
    assert dane_ostatniego_wiersza[3] == str(ed["age"])
    assert dane_ostatniego_wiersza[4] == ed["position"]
    assert dane_ostatniego_wiersza[5] == "✅" if ed["on_leave"] else "❌"



