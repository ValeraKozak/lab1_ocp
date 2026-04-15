from abc import ABC, abstractmethod

class IDatabase(ABC):
    @abstractmethod
    def get_employees(self):
        pass

    @abstractmethod
    def save_employees(self, employees):
        pass
