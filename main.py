import data.sql_server_db
import data.mongo_db
import data.excel_db

from factories.database_factory import DatabaseFactory
from services.employee_service import EmployeeService
from builders.employee_builder import EmployeeBuilder

def create_new_departments_from_prototype(source_department_employees):
    if len(source_department_employees) < 4:
        raise ValueError(
            "The source department must contain at least 4 employees: "
            "Manager, OfficeClerk, SalesManager and SysAdmin."
        )

    clone_hr = [employee.clone() for employee in source_department_employees]
    clone_fin = [employee.clone() for employee in source_department_employees]

    hr_names = ["Ivan Koval", "Olha Romaniuk", "Petro Sales", "Taras Admin"]
    fin_names = ["Maria Bondar", "Ihor Klym", "Oleh Trade", "Sofia Net"]

    for index, employee in enumerate(clone_hr):
        employee.id = 100 + index + 1
        employee.name = hr_names[index]
        employee.department = "HR"

    for index, employee in enumerate(clone_fin):
        employee.id = 200 + index + 1
        employee.name = fin_names[index]
        employee.department = "Finance"

    return clone_hr, clone_fin

def create_additional_employees_with_builder():
    builder = EmployeeBuilder()
    reserve = [
        builder.build_manager(301, "Roman Director", "Reserve", 33000, 5000).get_result(),
        builder.build_office_clerk(302, "Nadia Clerk", "Reserve", 185, 160).get_result(),
        builder.build_sales_manager(303, "Arsen Seller", "Reserve", 22000, 0.04, 90000).get_result(),
        builder.build_sys_admin(304, "Denys Support", "Reserve", 29000, 10, 350).get_result(),
    ]
    return reserve

def main():
    print("Choose DB: sql | mongo | excel")
    db_type = input("> ").strip().lower()

    db = DatabaseFactory.create_database(db_type)
    employees = db.get_employees()

    if not employees:
        raise RuntimeError("Database is empty.")

    source_department = employees[0].department
    source_department_employees = [e for e in employees if e.department == source_department]

    hr_department, finance_department = create_new_departments_from_prototype(source_department_employees)
    all_employees = source_department_employees + hr_department + finance_department

    # Builder is implemented and demonstrated here
    _builder_demo = create_additional_employees_with_builder()

    db.save_employees(all_employees)

    service = EmployeeService(all_employees)

    print("\n=== EMPLOYEES ===")
    for employee in all_employees:
        print(employee)

    print("\n=== ANALYTICS ===")
    print("Average salary (all departments):", round(service.average_salary(), 2))
    for department in sorted(service.count_by_department().keys()):
        print(f"Average salary ({department}):", round(service.average_salary_by_department(department), 2))
    print("Employees by department:", service.count_by_department())
    print("Average compensation by type:", service.compensation_by_type())

    chart_path = service.plot_department_distribution()
    print("Chart saved to:", chart_path)
    print("\nDone.")

if __name__ == "__main__":
    main()
