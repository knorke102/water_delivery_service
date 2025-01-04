import re
import tkinter as tk
from tkinter import ttk, messagebox

class AddDeliveryWindow:
    def __init__(self, parent, delivery_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить доставку")
        self.delivery_model = delivery_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о доставке", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="ID заказа").pack()
        self.order_id_entry = tk.Entry(self.window)
        self.order_id_entry.pack(pady=5)

        tk.Label(self.window, text="Дата доставки").pack()
        self.delivery_date_entry = tk.Entry(self.window)
        self.delivery_date_entry.pack(pady=5)

        tk.Label(self.window, text="Имя водителя").pack()
        self.driver_name_entry = tk.Entry(self.window)
        self.driver_name_entry.pack(pady=5)

        tk.Label(self.window, text="Номер автомобиля").pack()
        self.vehicle_number_entry = tk.Entry(self.window)
        self.vehicle_number_entry.pack(pady=5)

        tk.Label(self.window, text="Статус").pack()
        self.status_combobox = ttk.Combobox(self.window, values=["Доставлен", "Не доставлен"], state="readonly")
        self.status_combobox.pack(pady=5)
        self.status_combobox.set("Доставлен")

        tk.Button(self.window, text="Добавить доставку", width=30, command=self.add_delivery).pack(pady=10)

    def add_delivery(self):
        order_id = self.order_id_entry.get()
        delivery_date = self.delivery_date_entry.get()
        delivery_status = self.status_combobox.get()
        driver_name = self.driver_name_entry.get()
        vehicle_number = self.vehicle_number_entry.get()

        # Проверка корректности данных
        if not order_id or not delivery_date or not delivery_status or not driver_name or not vehicle_number:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        # Проверка ID заказа
        if not order_id.isdigit():
            messagebox.showerror("Ошибка", "ID клиента должно быть числом!")
            return

        # Проверка формата даты (например, "YYYY-MM-DD")
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, delivery_date):
            messagebox.showerror("Ошибка", "Неверный формат даты! Используйте формат: YYYY-MM-DD")
            return

        # Проверка имени (должно содержать только буквы)
        if not driver_name.isalpha():
            messagebox.showerror("Ошибка", "Имя водителя должно содержать только буквы!")
            return

        # Проверка номера транспортного средства
        vehicle_number_pattern = r"^[A-Za-z]{1,2}\d{3}[A-Za-z]{2}\d{2}$"
        if not re.match(vehicle_number_pattern, vehicle_number):
            messagebox.showerror("Ошибка", "Номер автомобиля: A123BC77")
            return

        # Если все проверки пройдены, добавляем доставку
        self.delivery_model.create(int(order_id), delivery_date, delivery_status, driver_name, vehicle_number)
        messagebox.showinfo("Успех", "Доставка добавлена успешно!")
        self.window.destroy()
