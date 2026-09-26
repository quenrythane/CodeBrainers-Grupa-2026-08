from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.logowanie_ui_v2
@pytest.mark.test_ui
def test_logowanie_ui_v2():
    # Arrange
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://127.0.0.1:8000/")

    # Act
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)


    # Assert
    assert driver.find_element(By.ID, "form-title").is_displayed()
    Select(driver.find_element(By.ID, "position")).select_by_visible_text("Junior QA")
    input()