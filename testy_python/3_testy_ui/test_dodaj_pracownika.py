from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.dodaj_pracownika
@pytest.mark.test_ui
def test_dodaj_pracownika(driver, employee_data, logowanie_ui):
    ed = employee_data

    # selectors
    name_input = (By.ID, "name")
    salary_input = (By.ID, "salary")
    age_input = (By.ID, "age")
    position_select = (By.ID, "position")
    on_vacation_checkbox = (By.ID, "on_leave")
    add_btn = (By.ID, "submitBtn")

    # akcje
    def fill_name_input(name: str):
        driver.find_element(*name_input).send_keys(name)

    def fill_salary_input(salary: int):
        driver.find_element(*salary_input).send_keys(salary)
    #   driver.find_element(*salary_input).send_keys(ed["salary"])

    def fill_age_input(age: int):
        driver.find_element(*age_input).send_keys(age)

    def fill_position_input(position: str):
        Select(driver.find_element(*position_select)).select_by_visible_text(position)

    def fill_on_vacation_checkbox(on_leave: bool):
        driver.find_element(*on_vacation_checkbox).click() if on_leave else None

    def fill_add_btn():
        driver.find_element(*add_btn).click()

    def fill_all_inputs(name: str, salary: int, age: int, position: str, on_leave: bool):
        fill_name_input(name)
        fill_salary_input(salary)
        fill_age_input(age)
        fill_position_input(position)
        fill_on_vacation_checkbox(on_leave)

    def get_data_from_last_row():
        tabela = driver.find_element(By.ID, "employees")
        ostatni_wiersz_tabeli = tabela.find_elements(By.TAG_NAME, "tr")[-1]
        komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
        # TODO: poniższe List comprehension zwraca błąd "StaleElementReferenceException". Naprawić poprzez EC.
        dane_ostatniego_wiersza = [element.text for element in komorki_ostatniego_wiersza][:-1]
        return dane_ostatniego_wiersza




    # Act
    fill_name_input(ed["name"])
    fill_salary_input(ed["salary"])
    fill_age_input(ed["age"])
    fill_position_input(ed["position"])
    fill_on_vacation_checkbox(ed["on_leave"])
    fill_add_btn()


    # Assert
    dane_ostatniego_wiersza = get_data_from_last_row()

    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == ed["name"]
    assert dane_ostatniego_wiersza[2] == str(ed["salary"])
    assert dane_ostatniego_wiersza[3] == str(ed["age"])
    assert dane_ostatniego_wiersza[4] == ed["position"]
    assert dane_ostatniego_wiersza[5] == "✅" if ed["on_leave"] else "❌"



