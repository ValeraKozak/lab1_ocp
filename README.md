# Лабораторна 1. Архітектура ПЗ

## Реалізовано
- Factory Method
- Prototype
- Singleton
- Builder
- Багатошарова архітектура
- 3 джерела даних: SQL Server / MongoDB / Excel
- 4 типи працівників: Manager, OfficeClerk, SalesManager, SysAdmin
- Статистичний аналіз: середня зарплата, середня по відділах, кількість по відділах, графік

## Початкові дані
У базі є один відділ `IT`, в якому є 4 типи працівників:
- Manager
- OfficeClerk
- SalesManager
- SysAdmin

На основі цих працівників програма створює ще 2 нові відділи:
- HR
- Finance

Отже фінальний результат — 3 відділи:
- IT (з БД)
- HR (створений програмою)
- Finance (створений програмою)

## Запуск через Excel
1. `pip install -r requirements.txt`
2. `python main.py`
3. Обрати `excel`

## Запуск через MongoDB
1. Запустити MongoDB
2. У `mongosh` виконати: `load('sql/mongo_seed.js')`
3. Запустити `python main.py`
4. Обрати `mongo`

## Запуск через SQL Server
1. У SSMS виконати:
   - `sql/01_create_db_and_table.sql`
   - `sql/02_seed_department.sql`
2. Запустити `python main.py`
3. Обрати `sql`

## Примітка
Builder у проєкті реалізований окремо і демонструється в `main.py`.
Для фінального набору даних у БД зберігаються лише 3 відділи:
один з БД і два створені програмою.
