import pyodbc
from data.database_base import IDatabase
from factories.employee_factory import EmployeeFactory
from data.singleton_connection import SQLServerConnectionManager

class SQLServerDB(IDatabase):
    def __init__(self):
        self.connection_manager = SQLServerConnectionManager(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=CompanyDB;Trusted_Connection=yes;"
        )

    def _connect(self):
        return pyodbc.connect(self.connection_manager.connection_string)

    def get_employees(self):
        employees = []
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, name, department, type, base_salary, bonus,
                       hourly_rate, hours_per_month, commission_rate,
                       monthly_sales, on_call_hours, on_call_rate
                FROM Employees
                ORDER BY id
                '''
            )
            rows = cur.fetchall()

            for row in rows:
                data = {
                    "id": row[0],
                    "name": row[1],
                    "department": row[2],
                    "type": row[3],
                    "base_salary": row[4],
                    "bonus": row[5],
                    "hourly_rate": row[6],
                    "hours_per_month": row[7],
                    "commission_rate": row[8],
                    "monthly_sales": row[9],
                    "on_call_hours": row[10],
                    "on_call_rate": row[11],
                }
                employees.append(EmployeeFactory.create_employee(data))
        return employees

    def save_employees(self, employees):
        with self._connect() as conn:
            cur = conn.cursor()
            for employee in employees:
                row = employee.to_dict()
                cur.execute(
                    '''
                    MERGE Employees AS target
                    USING (
                        SELECT ? AS id
                    ) AS source
                    ON target.id = source.id
                    WHEN MATCHED THEN
                        UPDATE SET
                            name = ?,
                            department = ?,
                            type = ?,
                            base_salary = ?,
                            bonus = ?,
                            hourly_rate = ?,
                            hours_per_month = ?,
                            commission_rate = ?,
                            monthly_sales = ?,
                            on_call_hours = ?,
                            on_call_rate = ?
                    WHEN NOT MATCHED THEN
                        INSERT (id, name, department, type, base_salary, bonus,
                                hourly_rate, hours_per_month, commission_rate,
                                monthly_sales, on_call_hours, on_call_rate)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    ''',
                    row["id"],
                    row["name"], row["department"], row["type"],
                    row["base_salary"], row["bonus"], row["hourly_rate"],
                    row["hours_per_month"], row["commission_rate"], row["monthly_sales"],
                    row["on_call_hours"], row["on_call_rate"],
                    row["id"], row["name"], row["department"], row["type"],
                    row["base_salary"], row["bonus"], row["hourly_rate"],
                    row["hours_per_month"], row["commission_rate"], row["monthly_sales"],
                    row["on_call_hours"], row["on_call_rate"]
                )
            conn.commit()

from factories.database_factory import DatabaseFactory

DatabaseFactory.register("sql", SQLServerDB)
