from db import connect_db

class Order:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, id_client, order_date, delivery_date, status, bottle_count):
        self.cursor.execute('''
            INSERT INTO orders (id_client, order_date, delivery_date, status, bottle_count)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_client, order_date, delivery_date, status, bottle_count))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM orders')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
