import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wymuszenie kodowania UTF-8 w systemie Windows dla zapisywania raportu w pytest-html 3.2.0
os.environ["PYTHONUTF8"] = "1"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 3)

@pytest.fixture
def logowanie_ui(driver, wait):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.XPATH, "//*[@id='loginForm']/button").click()
    assert wait.until(EC.visibility_of_element_located((By.ID, "form-title"))).is_displayed()


@pytest.fixture
def employee_data():
    return {
        "name": "Basia",
        "salary": 10_000,
        "age": 30,
        "position": "Junior QA",
        "on_leave": True
        }