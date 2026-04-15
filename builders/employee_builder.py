from models.manager import Manager
from models.office_clerk import OfficeClerk
from models.sales_manager import SalesManager
from models.sys_admin import SysAdmin

class EmployeeBuilder:
    def __init__(self):
        self.employee = None

    def build_manager(self, id, name, department, base_salary, bonus):
        self.employee = Manager(id, name, department, base_salary, bonus)
        return self

    def build_office_clerk(self, id, name, department, hourly_rate, hours_per_month):
        self.employee = OfficeClerk(id, name, department, hourly_rate, hours_per_month)
        return self

    def build_sales_manager(self, id, name, department, base_salary, commission_rate, monthly_sales):
        self.employee = SalesManager(id, name, department, base_salary, commission_rate, monthly_sales)
        return self

    def build_sys_admin(self, id, name, department, base_salary, on_call_hours, on_call_rate):
        self.employee = SysAdmin(id, name, department, base_salary, on_call_hours, on_call_rate)
        return self

    def get_result(self):
        if self.employee is None:
            raise ValueError("Employee has not been built yet.")
        return self.employee
