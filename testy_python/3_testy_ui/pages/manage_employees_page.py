from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ManageEmployeesPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
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
        self.type_text(self.name_input, name)

    def fill_salary(self, salary):
        self.type_text(self.salary_input, salary)

    def fill_age(self, age):
        self.type_text(self.age_input, age)

    def fill_position(self, position):
        self.select_by_visible_text(self.position_input, position)

    def fill_on_leave(self, on_leave):
        self.click(self.on_leave_input) if on_leave else None

    def submit_form(self):
        self.click(self.submit_input)

    def get_last_employee_data(self):
        tabela = self.find_visible_element(self.employees_table)
        self.wait.until(EC.visibility_of_element_located(self.employee_tr))
        wiersze = tabela.find_elements(*self.employee_tr)
        ostatni_wiersz_tabeli = wiersze[-1]
        komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(*self.employee_td)
        return [element.text for element in komorki_ostatniego_wiersza][:-1]