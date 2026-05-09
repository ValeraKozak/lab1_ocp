# Лабораторна робота 1: Архітектура та патерни проєктування

## Опис проєкту

Цей проєкт є лабораторною роботою з архітектури програмного забезпечення та патернів проєктування.
Програма вміє підключатися до одного з трьох джерел даних:

- `SQL Server`
- `MongoDB`
- `Excel`

Із вибраного джерела програма зчитує працівників одного відділу, після чого створює ще два додаткові відділи програмно та виконує базовий статистичний аналіз.

У проєкті продемонстровано:

- `Factory Method`
- `Prototype`
- `Singleton`
- `Builder`
- `Layered Architecture`

У системі реалізовано такі ролі працівників:

- `Manager`
- `OfficeClerk`
- `SalesManager`
- `SysAdmin`

## Основна ідея завдання

Програма отримує дані про працівників із вибраної бази даних.
Початкові дані містять один відділ, у якому є працівники чотирьох ролей.

Після цього програма:

1. зчитує працівників із вибраного джерела даних;
2. обирає по одному представнику кожної необхідної ролі;
3. створює один новий відділ за допомогою патерна `Prototype`;
4. створює ще один новий відділ за допомогою патерна `Builder`;
5. об’єднує працівників усіх трьох відділів;
6. обчислює статистичні показники;
7. будує графік кількості працівників за відділами.

У результаті отримуємо дані для трьох відділів:

- початковий відділ із бази даних;
- `HR`, створений програмою;
- `Finance`, створений програмою.

## Реалізована архітектура

Проєкт побудований за ідеєю `Layered Architecture`.
Відповідальність розділена на окремі логічні шари.

### 1. Шар представлення / координації

Файл: [main.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/main.py:1)

Цей файл координує роботу всієї програми:

- запитує в користувача, яку базу даних використати;
- отримує відповідне джерело даних із фабрики;
- завантажує працівників;
- створює два додаткові відділи;
- викликає шар бізнес-логіки;
- виводить результати та зберігає графік.

### 2. Шар бізнес-логіки

Файл: [employee_service.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/services/employee_service.py:1)

Цей шар містить аналітичні операції:

- середня зарплата для всіх працівників;
- середня зарплата по відділу;
- кількість працівників по відділах;
- середня компенсація за типом працівника;
- побудова графіка.

### 3. Шар доступу до даних

Папка: `data/`

Цей шар відповідає за роботу з джерелами даних:

- [sql_server_db.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/data/sql_server_db.py:1)
- [mongo_db.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/data/mongo_db.py:1)
- [excel_db.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/data/excel_db.py:1)

Кожен клас реалізує спільний інтерфейс бази даних і вміє:

- зчитувати працівників;
- зберігати працівників.

### 4. Доменний шар

Папка: `models/`

У цьому шарі знаходяться сутності працівників та логіка обчислення їхньої зарплати:

- [employee.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/models/employee.py:1)
- [manager.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/models/manager.py:1)
- [office_clerk.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/models/office_clerk.py:1)
- [sales_manager.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/models/sales_manager.py:1)
- [sys_admin.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/models/sys_admin.py:1)

Кожна роль має власні поля та власну реалізацію `compensation()`.

### 5. Шар створення об’єктів

Папки:

- `factories/`
- `builders/`

Ці модулі відповідають за створення об’єктів і допомагають ізолювати решту програми від конкретних реалізацій.

## Використані патерни

## Factory Method

### DatabaseFactory

Файл: [database_factory.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/factories/database_factory.py:1)

Призначення:

- обирає, який саме об’єкт джерела даних створити;
- приховує конкретні класи баз даних від решти програми;
- підтримує розширення новими типами БД.

Як це працює:

- адаптери баз даних реєструють себе в `DatabaseFactory`;
- `main.py` звертається до фабрики за базою за її назвою;
- фабрика повертає екземпляр потрібного класу.

Важлива деталь:

Фабрика автоматично знаходить модулі всередині `data/`.
Завдяки цьому нову базу можна додати, створивши новий файл `*_db.py` і зареєструвавши його, без змін у `main.py`.

### EmployeeFactory

Файл: [employee_factory.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/factories/employee_factory.py:1)

Призначення:

- створює об’єкти працівників із сирих словників даних;
- прибирає ланцюжки `if` із прикладної логіки;
- відповідає принципу `Open/Closed Principle`.

Як це працює:

- моделі працівників автоматично підтягуються з `models/`;
- кожна роль сама надає свій метод `from_data(...)`;
- фабрика делегує створення об’єкта відповідній ролі.

Це означає, що:

- для додавання нової ролі не потрібно змінювати `create_employee()`;
- достатньо додати новий клас моделі.

## Prototype

Файл: [employee.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/models/employee.py:1)

Реалізація:

- базовий клас `Employee` має метод `clone()`;
- `clone()` використовує глибоке копіювання;
- у `main.py` відділ `HR` створюється клонуванням шаблонних працівників із подальшою зміною `id`, `name` та `department`.

Чому це відповідає патерну:

- нові об’єкти створюються шляхом копіювання вже існуючих, а не ручного конструювання з нуля.

## Singleton

Файл: [singleton_connection.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/data/singleton_connection.py:1)

У проєкті є дві реалізації singleton:

- `SQLServerConnectionManager`
- `MongoClientSingleton`

Що саме є singleton у цьому проєкті:

- для SQL Server: один спільний об’єкт конфігурації підключення;
- для MongoDB: один спільний `MongoClient`.

Потокобезпечна реалізація:

- використовує `threading.Lock()`;
- захищає перше створення singleton-екземпляра.

Також у коді є:

- короткий Pythonic-приклад singleton у коментарі, як вимагав рецензент.

## Builder

Файл: [employee_builder.py](C:/Users/vkoza/OneDrive/Desktop/lab1_architecture_updated/builders/employee_builder.py:1)

Призначення:

- будує об’єкти працівників через окремий спеціалізований клас;
- дозволяє створювати працівників або з набору даних, або через динамічні методи `build_<role>()`.

Як він використовується у проєкті:

- відділ `Finance` створюється через builder;
- `main.py` бере шаблонних працівників, змінює їхні дані та повторно створює їх через `EmployeeBuilder`.

Важлива деталь:

Builder зроблений розширюваним.
Коли нова роль правильно додається в `models/`, builder може працювати з нею без зміни своєї основної логіки.

## Ролі працівників і логіка зарплати

### Manager

Поля:

- `id`
- `name`
- `department`
- `base_salary`
- `bonus`

Формула:

- `compensation = base_salary + bonus`

### OfficeClerk

Поля:

- `id`
- `name`
- `department`
- `hourly_rate`
- `hours_per_month`

Формула:

- `compensation = hourly_rate * hours_per_month`

### SalesManager

Поля:

- `id`
- `name`
- `department`
- `base_salary`
- `commission_rate`
- `monthly_sales`

Формула:

- `compensation = base_salary + commission_rate * monthly_sales`

### SysAdmin

Поля:

- `id`
- `name`
- `department`
- `base_salary`
- `on_call_hours`
- `on_call_rate`

Формула:

- `compensation = base_salary + on_call_hours * on_call_rate`

## Структура проєкту

```text
lab1_architecture_updated/
|-- builders/
|   `-- employee_builder.py
|-- data/
|   |-- database_base.py
|   |-- excel_db.py
|   |-- mongo_db.py
|   |-- singleton_connection.py
|   `-- sql_server_db.py
|-- factories/
|   |-- database_factory.py
|   `-- employee_factory.py
|-- models/
|   |-- employee.py
|   |-- manager.py
|   |-- office_clerk.py
|   |-- sales_manager.py
|   `-- sys_admin.py
|-- services/
|   `-- employee_service.py
|-- sql/
|   |-- 01_create_db_and_table.sql
|   |-- 02_seed_department.sql
|   `-- mongo_seed.js
|-- employees.xlsx
|-- main.py
|-- requirements.txt
`-- README.md
```

## Як працює програма покроково

1. Користувач запускає програму.
2. `DatabaseFactory` показує доступні джерела даних.
3. Створюється адаптер вибраної бази даних.
4. Працівники завантажуються з джерела.
5. Програма вибирає по одному шаблонному працівнику для кожної ролі.
6. Новий відділ `HR` створюється через `Prototype`.
7. Новий відділ `Finance` створюється через `Builder`.
8. Усі працівники об’єднуються в один список.
9. `EmployeeService` виконує обчислення статистики.
10. Програма виводить результати та зберігає графік у `employees_by_department.png`.

## Як запустити проєкт

## 1. Встановлення залежностей

```bash
pip install -r requirements.txt
```

Якщо використовується локальне віртуальне середовище:

```bash
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Запуск програми

```bash
python main.py
```

Програма запропонує вибрати одне з доступних джерел:

- `excel`
- `mongo`
- `sql`

## Запуск через Excel

Це найпростіший варіант для демонстрації.

Необхідно:

- файл `employees.xlsx` має існувати;
- файл не повинен бути відкритий у Microsoft Excel під час виконання програми, інакше він може бути заблокований.

Кроки:

1. встановити залежності;
2. запустити `python main.py`;
3. ввести `excel`.

## Запуск через MongoDB

Необхідно:

- встановлений і запущений MongoDB;
- доступ до `mongosh`.

Кроки:

1. запустити MongoDB;
2. відкрити `mongosh`;
3. виконати:

```javascript
load('sql/mongo_seed.js')
```

4. запустити:

```bash
python main.py
```

5. ввести `mongo`.

## Запуск через SQL Server

Необхідно:

- встановлений SQL Server;
- встановлений `ODBC Driver 17 for SQL Server`;
- доступ через Windows authentication.

Кроки:

1. відкрити SQL Server Management Studio;
2. виконати:

- `sql/01_create_db_and_table.sql`
- `sql/02_seed_department.sql`

3. запустити:

```bash
python main.py
```

4. ввести `sql`.

## Що виводить програма

У результаті програма формує:

- список працівників усіх трьох відділів у консолі;
- середню зарплату для всіх відділів разом;
- середню зарплату по кожному відділу;
- кількість працівників по відділах;
- середню компенсацію за типом працівника;
- файл графіка `employees_by_department.png`.

## Як додати нову базу даних

Щоб додати новий адаптер бази даних:

1. створити новий файл у `data/`, наприклад `postgres_db.py`;
2. реалізувати спільний інтерфейс із `database_base.py`;
3. зареєструвати адаптер у `DatabaseFactory`;
4. назвати файл так, щоб він закінчувався на `_db.py`.

Оскільки `DatabaseFactory` автоматично сканує пакет `data/`, змінювати `main.py` не потрібно.

## Як додати нову роль працівника

Щоб додати нову роль:

1. створити новий файл у `models/`, наприклад `qa_engineer.py`;
2. успадкуватися від `Employee`;
3. визначити:

- `type_name`
- `build_fields`
- `from_data(...)`
- `compensation()`
- `to_dict()`

Після цього:

- `EmployeeFactory` зможе автоматично створювати нову роль;
- `EmployeeBuilder` теж зможе з нею працювати;
- існуючу логіку фабрики змінювати не доведеться.

Важлива примітка:

Якщо нова роль має нові поля, яких ще немає у поточному форматі збереження, то може знадобитися розширення фізичного сховища:

- SQL-таблиці;
- Excel-стовпців;
- Mongo-документів.

Це вже питання рівня зберігання даних, а не фабрики.
