from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.logowanie_ui
@pytest.mark.test_ui
def test_logowanie_ui():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    # input("Wciśnij Enter, aby zamknąć przeglądarkę")

    # By.ID
    # By.CLASS_NAME
    # By.CSS_SELECTOR
    # By.LINK_TEXT
    # By.PARTIAL_LINK_TEXT
    # By.TAG_NAME
    # By.XPATH
    # By.NAME

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    # driver.find_element(By.CSS_SELECTOR, "#loginForm > button").click()
    # driver.find_element(By.XPATH, "/html/body/div/form/button").click()  # full xpath
    driver.find_element(By.XPATH, "//*[@id='loginForm']/button").click()  # relative xpath
    input("Wciśnij Enter, aby zamknąć przeglądarkę")


