from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.dodaj_pracownika
@pytest.mark.test_ui
def test_dodaj_pracownika():
    # Arrange
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://127.0.0.1:8000/")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.XPATH, "//*[@id='loginForm']/button").click()
    assert driver.find_element(By.ID, "form-title").is_displayed()

    # Act
    driver.find_element(By.ID, "name").send_keys("Basia")
    driver.find_element(By.ID, "salary").send_keys(10_000)
    driver.find_element(By.ID, "age").send_keys(30)
    Select(driver.find_element(By.ID, "position")).select_by_visible_text("Junior QA")
    driver.find_element(By.ID, "on_leave").click()
    driver.find_element(By.ID, "submitBtn").click()

    # Assert
    tabela = driver.find_element(By.ID, "employees")
    wiersze_tabeli = tabela.find_elements(By.TAG_NAME, "tr")
    ostatni_wiersz_tabeli = wiersze_tabeli[-1]
    komorka_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
    print(komorka_ostatniego_wiersza)  # zwraca listę nieczytelnych obiektów Selenium elementów
    dane_ostatniego_wiersza = [element.text for element in komorka_ostatniego_wiersza][:-1]
    print(dane_ostatniego_wiersza)  # zwraca ['1', 'Artur', '10000', '30', 'Junior QA', '✅']

    assert dane_ostatniego_wiersza[0] == "2"
    assert dane_ostatniego_wiersza[1] == "Basia"
    assert dane_ostatniego_wiersza[2] == "10000"
    assert dane_ostatniego_wiersza[3] == "30"
    assert dane_ostatniego_wiersza[4] == "Junior QA"
    assert dane_ostatniego_wiersza[5] == "✅"



