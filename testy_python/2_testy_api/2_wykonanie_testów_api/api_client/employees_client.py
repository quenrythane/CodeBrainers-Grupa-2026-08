from .base_api_client import BaseAPIClient

class EmployeesAPIClient(BaseAPIClient):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/employees"

    def create_employee(self, create_employee_correct_payload):
        return self.post(self.endpoint, payload=create_employee_correct_payload)


