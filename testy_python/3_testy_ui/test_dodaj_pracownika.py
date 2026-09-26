from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.dodaj_pracownika
@pytest.mark.test_ui
def test_dodaj_pracownika(driver, employee_data, logowanie_ui):
    # Act
    driver.find_element(By.ID, "name").send_keys(employee_data["name"])
    driver.find_element(By.ID, "salary").send_keys(employee_data["salary"])
    driver.find_element(By.ID, "age").send_keys(employee_data["age"])
    Select(driver.find_element(By.ID, "position")).select_by_visible_text(employee_data["position"])
    driver.find_element(By.ID, "on_leave").click() if employee_data["on_leave"] else None
    driver.find_element(By.ID, "submitBtn").click()
    # input()

    # Assert
    tabela = driver.find_element(By.ID, "employees")
    ostatni_wiersz_tabeli = tabela.find_elements(By.TAG_NAME, "tr")[-1]
    komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
    dane_ostatniego_wiersza = [element.text for element in komorki_ostatniego_wiersza][:-1]

    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == employee_data["name"]
    assert dane_ostatniego_wiersza[2] == str(employee_data["salary"])
    assert dane_ostatniego_wiersza[3] == str(employee_data["age"])
    assert dane_ostatniego_wiersza[4] == employee_data["position"]
    assert dane_ostatniego_wiersza[5] == "✅" if employee_data["on_leave"] else "❌"



