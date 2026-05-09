import importlib
import inspect
import pkgutil

from models.employee import Employee


class EmployeeFactory:
    _creators = {}
    _models = {}
    _discovered = False

    @classmethod
    def _discover_roles(cls):
        if cls._discovered:
            return

        import models

        for module_info in pkgutil.iter_modules(models.__path__):
            if module_info.name in {"employee", "__init__"}:
                continue
            importlib.import_module(f"models.{module_info.name}")

        for model_cls in Employee.__subclasses__():
            if inspect.isabstract(model_cls) or not model_cls.type_name:
                continue
            cls.register_model(model_cls)

        cls._discovered = True

    @classmethod
    def register(cls, employee_type, creator):
        cls._creators[Employee.canonical_type_name(employee_type)] = creator

    @classmethod
    def register_model(cls, model_cls):
        normalized_type = Employee.canonical_type_name(model_cls.type_name)
        cls._models[normalized_type] = model_cls
        cls.register(model_cls.type_name, lambda data, role=model_cls: role.from_data(dict(data)))

    @classmethod
    def create_employee(cls, data: dict):
        cls._discover_roles()
        emp_type = Employee.canonical_type_name(data["type"])
        creator = cls._creators.get(emp_type)

        if creator is None:
            raise ValueError(f"Unknown employee type: {data['type']}")

        return creator(data)

    @classmethod
    def get_build_fields(cls, employee_type):
        cls._discover_roles()
        normalized_type = Employee.canonical_type_name(employee_type)
        model_cls = cls._models.get(normalized_type)
        if model_cls is None:
            raise ValueError(f"Unknown employee type: {employee_type}")
        return model_cls.build_fields
