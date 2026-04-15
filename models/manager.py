from models.employee import Employee

class Manager(Employee):
    def __init__(self, id, name, department, base_salary, bonus):
        super().__init__(id, name, department)
        self.base_salary = float(base_salary)
        self.bonus = float(bonus)

    def compensation(self):
        return self.base_salary + self.bonus

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "type": "Manager",
            "base_salary": self.base_salary,
            "bonus": self.bonus,
            "hourly_rate": None,
            "hours_per_month": None,
            "commission_rate": None,
            "monthly_sales": None,
            "on_call_hours": None,
            "on_call_rate": None,
        }
