import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.get("http://127.0.0.1:8000/")
    yield driver
    driver.quit()

@pytest.fixture
def logowanie_ui(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.XPATH, "//*[@id='loginForm']/button").click()
    assert driver.find_element(By.ID, "form-title").is_displayed()


@pytest.fixture
def employee_data():
    return {
        "name": "Basia",
        "salary": 10_000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": True
        }