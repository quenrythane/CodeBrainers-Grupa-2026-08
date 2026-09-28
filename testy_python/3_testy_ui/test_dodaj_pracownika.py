from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.dodaj_pracownika
@pytest.mark.test_ui
def test_dodaj_pracownika(driver, employee_data, logowanie_ui, wait):
    # Arrange
    ed = employee_data
    name_input = (By.ID, "name")
    salary_input = (By.ID, "salary")
    age_input = (By.ID, "age")
    position_input = (By.ID, "position")
    on_leave_input = (By.ID, "on_leave")
    submit_input = (By.ID, "submitBtn")

    def fill_name(name):
        wait.until(EC.visibility_of_element_located(name_input)).send_keys(name)

    def fill_salary(salary):
        driver.find_element(*salary_input).send_keys(salary)

    def fill_age(age):
        driver.find_element(*age_input).send_keys(age)

    def fill_position(position):
        Select(driver.find_element(*position_input)).select_by_visible_text(position)

    def fill_on_leave(on_leave):
        driver.find_element(*on_leave_input).click() if on_leave else None

    def submit_form():
        driver.find_element(*submit_input).click()

    def get_last_employee_data():
        tabela = wait.until(
            EC.visibility_of_element_located((By.ID, "employees"))
            )
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tr")))
        ostatni_wiersz_tabeli = tabela.find_elements(By.TAG_NAME, "tr")[-1]
        komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
        return [element.text for element in komorki_ostatniego_wiersza][:-1]

    # Act
    fill_name(ed["name"])
    fill_salary(ed["salary"])
    fill_age(ed["age"])
    fill_position(ed["position"])
    fill_on_leave(ed["on_leave"])
    submit_form()

    # Assert
    dane_ostatniego_wiersza = get_last_employee_data()

    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == ed["name"]
    assert dane_ostatniego_wiersza[2] == str(ed["salary"])
    assert dane_ostatniego_wiersza[3] == str(ed["age"])
    assert dane_ostatniego_wiersza[4] == ed["position"]
    assert dane_ostatniego_wiersza[5] == ("✅" if ed["on_leave"] else "❌")



