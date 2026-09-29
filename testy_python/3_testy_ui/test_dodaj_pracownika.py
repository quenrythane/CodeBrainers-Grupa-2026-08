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



    # Act
    fill_name_input(ed["name"])
    
    driver.find_element(*salary_input).send_keys(ed["salary"])
    driver.find_element(*age_input).send_keys(ed["age"])
    Select(driver.find_element(*position_select)).select_by_visible_text(ed["position"])
    driver.find_element(*on_vacation_checkbox).click() if ed["on_leave"] else None
    driver.find_element(*add_btn).click()

    # employee_manger_page.fill_employee_name(ed["name"])



    # Assert
    tabela = driver.find_element(By.ID, "employees")
    ostatni_wiersz_tabeli = tabela.find_elements(By.TAG_NAME, "tr")[-1]
    komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
    # TODO: poniższe List comprehension zwraca błąd "StaleElementReferenceException". Naprawić poprzez EC.
    dane_ostatniego_wiersza = [element.text for element in komorki_ostatniego_wiersza][:-1]

    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == ed["name"]
    assert dane_ostatniego_wiersza[2] == str(ed["salary"])
    assert dane_ostatniego_wiersza[3] == str(ed["age"])
    assert dane_ostatniego_wiersza[4] == ed["position"]
    assert dane_ostatniego_wiersza[5] == "✅" if ed["on_leave"] else "❌"



