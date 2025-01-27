from db import connect_db

class Employee:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, name, role, phone, email, hire_date):
        self.cursor.execute('''
            INSERT INTO employees (name, role, phone, email, hire_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, role, phone, email, hire_date))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM employees')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
