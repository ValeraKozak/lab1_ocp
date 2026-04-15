from collections import Counter
import matplotlib.pyplot as plt

class EmployeeService:
    def __init__(self, employees):
        self.employees = employees

    def average_salary(self):
        if not self.employees:
            return 0.0
        return sum(emp.compensation() for emp in self.employees) / len(self.employees)

    def average_salary_by_department(self, department):
        filtered = [emp for emp in self.employees if emp.department == department]
        if not filtered:
            return 0.0
        return sum(emp.compensation() for emp in filtered) / len(filtered)

    def count_by_department(self):
        return dict(Counter(emp.department for emp in self.employees))

    def compensation_by_type(self):
        result = {}
        for emp in self.employees:
            result.setdefault(emp.__class__.__name__, []).append(emp.compensation())
        return {k: round(sum(v) / len(v), 2) for k, v in result.items()}

    def plot_department_distribution(self, out_path="employees_by_department.png"):
        data = self.count_by_department()
        plt.figure()
        plt.bar(data.keys(), data.values())
        plt.title("Employees per Department")
        plt.xlabel("Department")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(out_path, dpi=160)
        plt.close()
        return out_path
