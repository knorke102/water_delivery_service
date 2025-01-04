from db import connect_db

class Client:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, name, address, phone, email):
        self.cursor.execute('''
            INSERT INTO clients (name, address, phone, email)
            VALUES (?, ?, ?, ?)
        ''', (name, address, phone, email))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM clients')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
