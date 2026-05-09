from factories.database_factory import DatabaseFactory
from services.employee_service import EmployeeService
from builders.employee_builder import EmployeeBuilder


def select_role_templates(employees):
    templates = {}
    required_types = ("Manager", "OfficeClerk", "SalesManager", "SysAdmin")

    for employee in employees:
        templates.setdefault(employee.__class__.__name__, employee)

    missing_types = [employee_type for employee_type in required_types if employee_type not in templates]
    if missing_types:
        raise ValueError(f"Missing employee roles in source department: {', '.join(missing_types)}")

    return [templates[employee_type] for employee_type in required_types]


def create_department_with_prototype(source_department_employees, department_name, starting_id, names):
    if len(source_department_employees) < 4:
        raise ValueError(
            "The source department must contain at least 4 employees: "
            "Manager, OfficeClerk, SalesManager and SysAdmin."
        )
    if len(names) != len(source_department_employees):
        raise ValueError("Names list must match the number of employee templates.")

    clones = [employee.clone() for employee in source_department_employees]
    for index, employee in enumerate(clones):
        employee.id = starting_id + index + 1
        employee.name = names[index]
        employee.department = department_name
    return clones


def create_department_with_builder(source_department_employees, department_name, starting_id, names):
    if len(names) != len(source_department_employees):
        raise ValueError("Names list must match the number of employee templates.")

    builder = EmployeeBuilder()
    built_department = []

    for index, employee in enumerate(source_department_employees):
        data = employee.to_dict()
        data["id"] = starting_id + index + 1
        data["name"] = names[index]
        data["department"] = department_name
        built_department.append(builder.build_from_data(data).get_result())

    return built_department


def main():
    available_dbs = " | ".join(DatabaseFactory.available_databases())
    print(f"Choose DB: {available_dbs}")
    db_type = input("> ").strip().lower()

    db = DatabaseFactory.create_database(db_type)
    employees = db.get_employees()

    if not employees:
        raise RuntimeError("Database is empty.")

    source_department = employees[0].department
    source_department_employees = [e for e in employees if e.department == source_department]
    templates = select_role_templates(source_department_employees)

    hr_department = create_department_with_prototype(
        templates,
        "HR",
        100,
        ["Ivan Koval", "Olha Romaniuk", "Petro Sales", "Taras Admin"],
    )
    finance_department = create_department_with_builder(
        templates,
        "Finance",
        200,
        ["Maria Bondar", "Ihor Klym", "Oleh Trade", "Sofia Net"],
    )
    all_employees = source_department_employees + hr_department + finance_department

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
