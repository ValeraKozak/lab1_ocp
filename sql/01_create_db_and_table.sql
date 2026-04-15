IF DB_ID('CompanyDB') IS NULL
    CREATE DATABASE CompanyDB;
GO

USE CompanyDB;
GO

IF OBJECT_ID('dbo.Employees', 'U') IS NOT NULL
    DROP TABLE dbo.Employees;
GO

CREATE TABLE dbo.Employees (
    id INT PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    department NVARCHAR(100) NOT NULL,
    type NVARCHAR(50) NOT NULL,
    base_salary FLOAT NULL,
    bonus FLOAT NULL,
    hourly_rate FLOAT NULL,
    hours_per_month FLOAT NULL,
    commission_rate FLOAT NULL,
    monthly_sales FLOAT NULL,
    on_call_hours FLOAT NULL,
    on_call_rate FLOAT NULL
);
GO
