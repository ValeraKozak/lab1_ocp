from models.employee import Employee


class SalesManager(Employee):
    type_name = "SalesManager"
    build_fields = (
        "id",
        "name",
        "department",
        "base_salary",
        "commission_rate",
        "monthly_sales",
    )

    def __init__(self, id, name, department, base_salary, commission_rate, monthly_sales):
        super().__init__(id, name, department)
        self.base_salary = float(base_salary)
        self.commission_rate = float(commission_rate)
        self.monthly_sales = float(monthly_sales)

    @classmethod
    def from_data(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["department"],
            cls.as_number(data.get("base_salary")),
            cls.as_number(data.get("commission_rate")),
            cls.as_number(data.get("monthly_sales")),
        )

    def compensation(self):
        return self.base_salary + (self.commission_rate * self.monthly_sales)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "type": "SalesManager",
            "base_salary": self.base_salary,
            "bonus": None,
            "hourly_rate": None,
            "hours_per_month": None,
            "commission_rate": self.commission_rate,
            "monthly_sales": self.monthly_sales,
            "on_call_hours": None,
            "on_call_rate": None,
        }
