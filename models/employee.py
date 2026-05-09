import copy
from abc import ABC, abstractmethod


class Employee(ABC):
    type_name = None
    build_fields = ()

    def __init__(self, id, name, department):
        self.id = int(id)
        self.name = str(name)
        self.department = str(department)

    @staticmethod
    def canonical_type_name(value):
        return "".join(ch.lower() for ch in str(value) if ch.isalnum())

    @staticmethod
    def as_number(value, default=0.0):
        if value is None:
            return default
        text = str(value).strip().lower()
        if text in ("", "nan", "none"):
            return default
        return float(value)

    @abstractmethod
    def compensation(self):
        raise NotImplementedError("Subclasses must implement compensation()")

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("Subclasses must implement to_dict()")

    @classmethod
    @abstractmethod
    def from_data(cls, data):
        raise NotImplementedError("Subclasses must implement from_data()")

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, department={self.department}, compensation={self.compensation():.2f})"
