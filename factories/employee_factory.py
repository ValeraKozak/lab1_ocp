from models.manager import Manager
from models.office_clerk import OfficeClerk
from models.sales_manager import SalesManager
from models.sys_admin import SysAdmin

class EmployeeFactory:
    @staticmethod
    def _num(value, default=0.0):
        if value is None:
            return default
        text = str(value).strip().lower()
        if text in ("", "nan", "none"):
            return default
        return float(value)

    @staticmethod
    def create_employee(data: dict):
        emp_type = str(data["type"]).strip().lower()

        if emp_type == "manager":
            return Manager(
                data["id"], data["name"], data["department"],
                EmployeeFactory._num(data.get("base_salary")),
                EmployeeFactory._num(data.get("bonus"))
            )
        if emp_type == "officeclerk":
            return OfficeClerk(
                data["id"], data["name"], data["department"],
                EmployeeFactory._num(data.get("hourly_rate")),
                EmployeeFactory._num(data.get("hours_per_month"))
            )
        if emp_type == "salesmanager":
            return SalesManager(
                data["id"], data["name"], data["department"],
                EmployeeFactory._num(data.get("base_salary")),
                EmployeeFactory._num(data.get("commission_rate")),
                EmployeeFactory._num(data.get("monthly_sales"))
            )
        if emp_type == "sysadmin":
            return SysAdmin(
                data["id"], data["name"], data["department"],
                EmployeeFactory._num(data.get("base_salary")),
                EmployeeFactory._num(data.get("on_call_hours")),
                EmployeeFactory._num(data.get("on_call_rate"))
            )

        raise ValueError(f"Unknown employee type: {data['type']}")
