from selenium import webdriver
import pytest


@pytest.mark.site_title
def test_site_title():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")

    site_title = driver.title
    expected_title = "Login - Employee Manager"

    assert site_title == expected_title

    # input("Wciśnij Enter, aby zamknąć przeglądarkę")

