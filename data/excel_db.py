import pandas as pd
from data.database_base import IDatabase
from factories.employee_factory import EmployeeFactory

class ExcelDB(IDatabase):
    def __init__(self, path="employees.xlsx"):
        self.path = path

    def get_employees(self):
        employees = []
        df = pd.read_excel(self.path)
        for _, row in df.iterrows():
            data = {
                "id": row["id"],
                "name": row["name"],
                "department": row["department"],
                "type": row["type"],
                "base_salary": row.get("base_salary"),
                "bonus": row.get("bonus"),
                "hourly_rate": row.get("hourly_rate"),
                "hours_per_month": row.get("hours_per_month"),
                "commission_rate": row.get("commission_rate"),
                "monthly_sales": row.get("monthly_sales"),
                "on_call_hours": row.get("on_call_hours"),
                "on_call_rate": row.get("on_call_rate"),
            }
            employees.append(EmployeeFactory.create_employee(data))
        return employees

    def save_employees(self, employees):
        rows = [employee.to_dict() for employee in employees]
        df = pd.DataFrame(rows)
        df.to_excel(self.path, index=False)

from factories.database_factory import DatabaseFactory

DatabaseFactory.register("excel", ExcelDB)