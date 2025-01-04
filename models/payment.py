from db import connect_db

class Payment:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, id_order, payment_date, payment_amount, payment_method):
        self.cursor.execute('''
            INSERT INTO payments (id_order, payment_date, payment_amount, payment_method)
            VALUES (?, ?, ?, ?)
        ''', (id_order, payment_date, payment_amount, payment_method))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM payments')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
