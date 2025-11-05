


import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL NOT NULL, 
        department_id INTEGER,
        FOREIGN KEY(department_id) REFERENCES Department(id) ON DELETE SET NULL
    )
""")

conn.commit()


class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def save(self):
        cursor.execute("INSERT INTO Department (id, name) VALUES (?, ?)", (self.id, self.name))
        conn.commit()

    @staticmethod
    def all():
        cursor.execute("SELECT * FROM Department")
        return [Department(*row) for row in cursor.fetchall()]

class Employee:
    def __init__(self, id, name, salary, department_id=None):
        self.id = id
        self.name = name 
        self.salary = salary 
        self.department_id = department_id

    def save(self):
        cursor.execute(
            "INSERT INTO Employee (id, name, salary, department_id) VALUES (?, ?, ?, ?)",
            (self.id, self.name, self.salary, self.department_id)
        )
        conn.commit()

    @staticmethod
    def all():
        cursor.execute("SELECT * FROM Employee")
        return [Employee(*row) for row in cursor.fetchall()]

it = Department(1, "IT")
hr = Department(2, 'HR')

it.save()
hr.save()

emp1 = Employee(1, "Alice", 5000, 1)
emp2 = Employee(2, "Bob", 8000, 1)
emp3 = Employee(3, "Djon", 10000, 2)
emp1.save()
emp2.save()
emp3.save()

cursor.execute("""
    SELECT Department.name, AVG(Employee.salary)
    FROM Employee
    JOIN Department ON Employee.department_id = Department.id
    GROUP BY Department.id
""")
for row in cursor.fetchall():
    print(f"ОТдел {row[0]}, средняя зарплата: {row[1]}")

cursor.execute("""
SELECT name, salary
FROM Employee e1 
WHERE salary > (
    SELECT AVG(salary)
    FROM Employee e2
    WHERE e2.department_id = e1.department_id
    )
""")
print("Сотрудники с зарплатой выше среднего")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
    CREATE VIEW IF NOT EXISTS HighSalary AS 
    SELECT name, salary, department_id
    FROM Employee
    WHERE salary > 6000
""")

cursor.execute("SELECT * FROM HighSalary")
for row in cursor.fetchall():
    print(row)