from typing import Tuple, List
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    Locator = Tuple[str, str]

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logger = logging.getLogger(__name__)

    def open_url(self, url: str) -> None:
        self.logger.info(f"Nawigacja do URL: {url}")
        self.driver.get(url)

    def find_visible_element(self, locator: Locator) -> WebElement:
        self.logger.debug(f"Oczekiwanie na widoczność elementu: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Element nie stał się widoczny w wyznaczonym czasie: {locator}")
            raise TimeoutException(f"Element {locator} nie pojawił się na stronie.")

    def find_elements(self, locator: Locator) -> List[WebElement]:
        self.logger.debug(f"Wyszukiwanie elementów: {locator}")
        return self.driver.find_elements(*locator)

    def find_visible_elements(self, locator: Locator) -> List[WebElement]:
        self.logger.debug(f"Oczekiwanie na widoczność elementów: {locator}")
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Elementy nie stały się widoczne w wyznaczonym czasie: {locator}")
            raise TimeoutException(f"Brak widocznych elementów dla lokatora {locator}.")

    def find_elements_in_element(self, parent_element: WebElement, locator: Locator) -> List[WebElement]:
        self.logger.debug(f"Wyszukiwanie elementów podrzędnych dla {locator}")
        return parent_element.find_elements(*locator)

    def find_clickable_element(self, locator: Locator) -> WebElement:
        self.logger.debug(f"Oczekiwanie na klikalność elementu: {locator}")
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error(f"Element nie jest klikalny: {locator}")
            raise TimeoutException(f"Element {locator} nie stał się klikalny.")

    def click(self, locator: Locator) -> None:
        self.logger.info(f"Klikanie w element: {locator}")
        try:
            element = self.find_clickable_element(locator)
            element.click()
        except ElementClickInterceptedException:
            self.logger.warning(f"Kliknięcie przechwycone dla {locator}. Próba przewinięcia i kliknięcia przez JS.")
            self.scroll_to_element(locator)
            element = self.find_clickable_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator: Locator, text: str, clear_first: bool = True) -> None:
        self.logger.info(f"Wpisywanie tekstu '{text}' w pole {locator}")
        element = self.find_visible_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def select_by_visible_text(self, locator: Locator, text: str) -> None:
        self.logger.info(f"Wybieranie opcji '{text}' z listy: {locator}")
        element = self.find_visible_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def get_text(self, locator: Locator) -> str:
        element = self.find_visible_element(locator)
        text = element.text
        self.logger.info(f"Pobrany tekst z {locator}: '{text}'")
        return text

    def scroll_to_element(self, locator: Locator) -> WebElement:
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def is_element_displayed(self, locator: Locator, timeout: int = 3) -> bool:
        try:
            custom_wait = WebDriverWait(self.driver, timeout)
            return custom_wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False
