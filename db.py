import sqlite3
import os

def connect_db():
    """Создает подключение к базе данных SQLite."""
    db_path = os.path.join(os.path.dirname(__file__), 'migrations', 'gimranov_water_delivery_service.db')
    return sqlite3.connect(db_path)
