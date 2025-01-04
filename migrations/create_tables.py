from db import connect_db


def create_tables():
    """Создает все таблицы в базе данных."""
    conn = connect_db()
    cursor = conn.cursor()

    # Создание таблицы клиентов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id_client INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            phone TEXT,
            email TEXT)
    ''')

    # Создание таблицы заказов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id_order INTEGER PRIMARY KEY AUTOINCREMENT,
            id_client INTEGER,
            order_date TEXT,
            delivery_date TEXT,
            status TEXT,
            bottle_count INTEGER,
            FOREIGN KEY (id_client) REFERENCES clients(id_client)
        )
    ''')

    # Создание таблицы доставок
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS deliveries (
            id_delivery INTEGER PRIMARY KEY AUTOINCREMENT,
            id_order INTEGER,
            delivery_date TEXT,
            delivery_status TEXT,
            driver_name TEXT,
            vehicle_number TEXT,
            FOREIGN KEY (id_order) REFERENCES orders(id_order)
        )
    ''')

    # Создание таблицы платежей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id_payment INTEGER PRIMARY KEY AUTOINCREMENT,
            id_order INTEGER,
            payment_date TEXT,
            payment_amount REAL,
            payment_method TEXT,
            FOREIGN KEY (id_order) REFERENCES orders(id_order)
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
