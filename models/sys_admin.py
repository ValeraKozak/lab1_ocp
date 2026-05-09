from models.employee import Employee


class SysAdmin(Employee):
    type_name = "SysAdmin"
    build_fields = (
        "id",
        "name",
        "department",
        "base_salary",
        "on_call_hours",
        "on_call_rate",
    )

    def __init__(self, id, name, department, base_salary, on_call_hours, on_call_rate):
        super().__init__(id, name, department)
        self.base_salary = float(base_salary)
        self.on_call_hours = float(on_call_hours)
        self.on_call_rate = float(on_call_rate)

    @classmethod
    def from_data(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["department"],
            cls.as_number(data.get("base_salary")),
            cls.as_number(data.get("on_call_hours")),
            cls.as_number(data.get("on_call_rate")),
        )

    def compensation(self):
        return self.base_salary + (self.on_call_hours * self.on_call_rate)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "type": "SysAdmin",
            "base_salary": self.base_salary,
            "bonus": None,
            "hourly_rate": None,
            "hours_per_month": None,
            "commission_rate": None,
            "monthly_sales": None,
            "on_call_hours": self.on_call_hours,
            "on_call_rate": self.on_call_rate,
        }
