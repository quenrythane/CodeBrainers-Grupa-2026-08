from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class EmployeeManagerPage:
    def __init__(self, driver):
        self.driver = driver
        # selectors
        self.name_input = (By.ID, "name")
        self.salary_input = (By.ID, "salary")
        self.age_input = (By.ID, "age")
        self.position_select = (By.ID, "position")
        self.on_vacation_checkbox = (By.ID, "on_leave")
        self.add_btn = (By.ID, "submitBtn")

        self.employees_table = (By.ID, "employees")
        self.employees_table_rows = (By.TAG_NAME, "tr")
        self.employees_table_data = (By.TAG_NAME, "td")


    # akcje
    def fill_name_input(self, name: str):
        self.driver.find_element(*self.name_input).send_keys(name)

    def fill_salary_input(self, salary: int):
        self.driver.find_element(*self.salary_input).send_keys(salary)
    #   driver.find_element(*salary_input).send_keys(ed["salary"])

    def fill_age_input(self, age: int):
        self.driver.find_element(*self.age_input).send_keys(age)

    def select_position_select(self, position: str):
        Select(self.driver.find_element(*self.position_select)).select_by_visible_text(position)

    def click_on_vacation_checkbox(self, on_leave: bool):
        self.driver.find_element(*self.on_vacation_checkbox).click() if on_leave else None

    def click_add_btn(self):
        self.driver.find_element(*self.add_btn).click()

    def fill_all_inputs(self, name: str, salary: int, age: int, position: str, on_leave: bool):
        self.fill_name_input(name)
        self.fill_salary_input(salary)
        self.fill_age_input(age)
        self.fill_position_input(position)
        self.fill_on_vacation_checkbox(on_leave)

    def get_data_from_last_row(self):
        tabela = self.driver.find_element(*self.employees_table)
        ostatni_wiersz_tabeli = tabela.find_elements(*self.employees_table_rows)[-1]
        komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(*self.employees_table_data)
        # TODO: poniższe List comprehension zwraca błąd "StaleElementReferenceException". Naprawić poprzez EC.
        dane_ostatniego_wiersza = [element.text for element in komorki_ostatniego_wiersza][:-1]
        return dane_ostatniego_wiersza