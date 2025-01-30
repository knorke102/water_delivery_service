from db import connect_db

class Inventory:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, item_name, item_description, stock_quantity, unit_price):
        self.cursor.execute('''
            INSERT INTO inventory (item_name, item_description, stock_quantity, unit_price)
            VALUES (?, ?, ?, ?)
        ''', (item_name, item_description, stock_quantity, unit_price))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM inventory')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
