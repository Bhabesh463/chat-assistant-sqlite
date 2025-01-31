# First I created a database with following tables.
# SQLite Database (database.db) with Employees and Departments tables.


import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create Employees table as per suggested
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Department TEXT,
                        Salary INTEGER,
                        Hire_Date TEXT)''')

    # Insert sample data given in assignment
    employees_data = [
        (1, "Alice", "Sales", 50000, "2021-01-15"),
        (2, "Bob", "Engineering", 70000, "2020-06-10"),
        (3, "Charlie", "Marketing", 60000, "2022-03-20"),
    ]
    
    cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", employees_data)

    # Create Departments table as per suggested
    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Manager TEXT)''')

    # Insert sample data given in assignment
    departments_data = [
        (1, "Sales", "Alice"),
        (2, "Engineering", "Bob"),
        (3, "Marketing", "Charlie"),
    ]

    cursor.executemany("INSERT INTO Departments VALUES (?, ?,? )", departments_data)
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    create_database()

