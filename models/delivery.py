from db import connect_db

class Delivery:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, id_order, delivery_date, delivery_status, driver_name, vehicle_number):
        self.cursor.execute('''
            INSERT INTO deliveries (id_order, delivery_date, delivery_status, driver_name, vehicle_number)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_order, delivery_date, delivery_status, driver_name, vehicle_number))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM deliveries')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
