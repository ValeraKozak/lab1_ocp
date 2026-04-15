from models.employee import Employee

class OfficeClerk(Employee):
    def __init__(self, id, name, department, hourly_rate, hours_per_month):
        super().__init__(id, name, department)
        self.hourly_rate = float(hourly_rate)
        self.hours_per_month = float(hours_per_month)

    def compensation(self):
        return self.hourly_rate * self.hours_per_month

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "type": "OfficeClerk",
            "base_salary": None,
            "bonus": None,
            "hourly_rate": self.hourly_rate,
            "hours_per_month": self.hours_per_month,
            "commission_rate": None,
            "monthly_sales": None,
            "on_call_hours": None,
            "on_call_rate": None,
        }
