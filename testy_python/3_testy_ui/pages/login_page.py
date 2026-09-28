from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.name_input = (By.ID, "name")
        self.salary_input = (By.ID, "salary")
        self.age_input = (By.ID, "age")
        self.position_input = (By.ID, "position")
        self.on_leave_input = (By.ID, "on_leave")
        self.submit_input = (By.ID, "submitBtn")
        self.form_title = (By.ID, "form-title")
        self.employees_table = (By.ID, "employees")
        self.employee_tr = (By.TAG_NAME, "tr")
        self.employee_td = (By.TAG_NAME, "td")

    def fill_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.name_input)).send_keys(name)

    def fill_salary(self, salary):
        self.driver.find_element(*self.salary_input).send_keys(salary)

    def fill_age(self, age):
        self.driver.find_element(*self.age_input).send_keys(age)

    def fill_position(self, position):
        Select(self.driver.find_element(*self.position_input)).select_by_visible_text(position)

    def fill_on_leave(self, on_leave):
        self.driver.find_element(*self.on_leave_input).click() if on_leave else None

    def submit_form(self):
        self.driver.find_element(*self.submit_input).click()

    def get_last_employee_data(self):
        tabela = self.wait.until(
            EC.visibility_of_element_located(self.employees_table)
            )
        self.wait.until(EC.visibility_of_element_located(self.employee_tr))
        ostatni_wiersz_tabeli = tabela.find_elements(*self.employee_tr)[-1]
        komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(*self.employee_td)
        return [element.text for element in komorki_ostatniego_wiersza][:-1]