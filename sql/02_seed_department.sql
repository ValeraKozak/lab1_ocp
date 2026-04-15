USE CompanyDB;
GO

INSERT INTO dbo.Employees
(id, name, department, type, base_salary, bonus, hourly_rate, hours_per_month,
 commission_rate, monthly_sales, on_call_hours, on_call_rate)
VALUES
(1, 'Andrii Petrenko', 'IT', 'Manager', 30000, 5000, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Petro Bondar', 'IT', 'OfficeClerk', NULL, NULL, 180, 160, NULL, NULL, NULL, NULL),
(3, 'Olena Klymenko', 'IT', 'SalesManager', 22000, NULL, NULL, NULL, 0.05, 100000, NULL, NULL),
(4, 'Taras Hnatiuk', 'IT', 'SysAdmin', 28000, NULL, NULL, NULL, NULL, NULL, 20, 300);
GO
