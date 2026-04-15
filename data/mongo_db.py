from pymongo import MongoClient
from data.database_base import IDatabase
from factories.employee_factory import EmployeeFactory
from data.singleton_connection import SingletonConnection

class MongoDB(IDatabase):
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.singleton = SingletonConnection(uri)

    def _collection(self):
        client = MongoClient(self.singleton.connection_string)
        db = client["CompanyDB"]
        return db["employees"]

    def get_employees(self):
        employees = []
        col = self._collection()
        for doc in col.find({}, {"_id": 0}):
            employees.append(EmployeeFactory.create_employee(doc))
        return employees

    def save_employees(self, employees):
        col = self._collection()
        for employee in employees:
            row = employee.to_dict()
            col.update_one(
                {"id": row["id"]},
                {"$set": row},
                upsert=True
            )
from factories.database_factory import DatabaseFactory

DatabaseFactory.register("mongo", MongoDB)