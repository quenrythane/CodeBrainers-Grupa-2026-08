from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

# @pytest.mark.xfail(reason="flakky testy - czasami się wysypuje")
@pytest.mark.logowanie_ui
@pytest.mark.test_ui
def test_logowanie_ui():
    # Arrange
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://127.0.0.1:8000/")
    # input("Wciśnij Enter, aby zamknąć przeglądarkę")

    # sposoby wyszukiwania elementów:
    # By.ID
    # By.CLASS_NAME
    # By.CSS_SELECTOR
    # By.XPATH
    # By.LINK_TEXT
    # By.PARTIAL_LINK_TEXT
    # By.TAG_NAME
    # By.NAME

    # Act
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.XPATH, "//*[@id='loginForm']/button").click()  # relative xpath
    # alternatywne wyszukiwanie przycisku
    # driver.find_element(By.CSS_SELECTOR, "#loginForm > button").click()
    # driver.find_element(By.XPATH, "/html/body/div/form/button").click()  # full xpath

    # Assert
    # input("Wciśnij Enter, aby zamknąć przeglądarkę")
    assert driver.find_element(By.ID, "form-title").is_displayed()

    input("Wciśnij Enter, aby zamknąć przeglądarkę")
