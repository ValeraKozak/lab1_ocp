from factories.employee_factory import EmployeeFactory

class EmployeeBuilder:
    def __init__(self):
        self.employee = None

    def build(self, employee_type, **data):
        payload = dict(data)
        payload["type"] = employee_type
        self.employee = EmployeeFactory.create_employee(payload)
        return self

    def build_from_data(self, data):
        self.employee = EmployeeFactory.create_employee(data)
        return self

    def __getattr__(self, name):
        if not name.startswith("build_"):
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")

        employee_type = name[6:]
        fields = EmployeeFactory.get_build_fields(employee_type)

        def dynamic_builder(*args):
            if len(args) != len(fields):
                raise TypeError(
                    f"{name}() takes exactly {len(fields)} arguments, but {len(args)} were given"
                )
            data = dict(zip(fields, args))
            return self.build(employee_type, **data)

        return dynamic_builder

    def get_result(self):
        if self.employee is None:
            raise ValueError("Employee has not been built yet.")
        return self.employee
