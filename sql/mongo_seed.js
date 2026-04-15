db = db.getSiblingDB('CompanyDB');
db.employees.deleteMany({});

db.employees.insertMany([
  {
    id: 1,
    name: "Andrii Petrenko",
    department: "IT",
    type: "Manager",
    base_salary: 30000,
    bonus: 5000
  },
  {
    id: 2,
    name: "Petro Bondar",
    department: "IT",
    type: "OfficeClerk",
    hourly_rate: 180,
    hours_per_month: 160
  },
  {
    id: 3,
    name: "Olena Klymenko",
    department: "IT",
    type: "SalesManager",
    base_salary: 22000,
    commission_rate: 0.05,
    monthly_sales: 100000
  },
  {
    id: 4,
    name: "Taras Hnatiuk",
    department: "IT",
    type: "SysAdmin",
    base_salary: 28000,
    on_call_hours: 20,
    on_call_rate: 300
  }
]);
