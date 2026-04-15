import copy
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name, department):
        self.id = int(id)
        self.name = str(name)
        self.department = str(department)

    @abstractmethod
    def compensation(self):
        raise NotImplementedError("Subclasses must implement compensation()")

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("Subclasses must implement to_dict()")

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, department={self.department}, compensation={self.compensation():.2f})"
