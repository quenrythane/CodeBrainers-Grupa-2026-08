import os
import sys
import pytest
from datetime import datetime
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




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # 1. Zapis na dysk
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(screenshots_dir, f"{item.name}_{timestamp}.png")
            driver.save_screenshot(filename)
            # 2. Dołączenie obrazka do raportu HTML (w formacie base64)
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(report, "extra", [])
                screenshot_b64 = driver.get_screenshot_as_base64()
                html_img = f'<div><img src="data:image/png;base64,{screenshot_b64}" style="width:600px; border:1px solid red;" /></div>'
                extra.append(pytest_html.extras.html(html_img))
                report.extra = extra
