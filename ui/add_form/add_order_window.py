import re
import tkinter as tk
from tkinter import ttk, messagebox

class AddOrderWindow:
    def __init__(self, parent, order_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить заказ")
        self.order_model = order_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о заказе", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="ID клиента").pack()
        self.client_id_entry = tk.Entry(self.window)
        self.client_id_entry.pack(pady=5)

        tk.Label(self.window, text="Дата заказа").pack()
        self.order_date_entry = tk.Entry(self.window)
        self.order_date_entry.pack(pady=5)

        tk.Label(self.window, text="Дата доставки").pack()
        self.delivery_date_entry = tk.Entry(self.window)
        self.delivery_date_entry.pack(pady=5)

        tk.Label(self.window, text="Количество бутылей").pack()
        self.bottle_count_entry = tk.Entry(self.window)
        self.bottle_count_entry.pack(pady=5)

        tk.Label(self.window, text="Статус").pack()
        self.status_combobox = ttk.Combobox(self.window, values=["Новый", "Отклонен"], state="readonly")
        self.status_combobox.pack(pady=5)
        self.status_combobox.set("Новый")

        tk.Button(self.window, text="Добавить заказ", width=30, command=self.add_order).pack(pady=10)

    def add_order(self):
        client_id = self.client_id_entry.get()
        order_date = self.order_date_entry.get()
        delivery_date = self.delivery_date_entry.get()
        status = self.status_combobox.get()
        bottle_count = self.bottle_count_entry.get()

        # Проверка корректности данных
        if not client_id or not order_date or not delivery_date or not status or not bottle_count:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        # Проверка ID клиента
        if not client_id.isdigit():
            messagebox.showerror("Ошибка", "ID клиента должно быть числом!")
            return

        # Проверка формата даты (например, "YYYY-MM-DD")
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, order_date) and re.match(date_pattern, delivery_date):
            messagebox.showerror("Ошибка", "Неверный формат даты! Используйте формат: YYYY-MM-DD")
            return

        # Проверка количества бутылей
        if not bottle_count.isdigit():
            messagebox.showerror("Ошибка", "Количество бутылей должно быть числом!")
            return

        # Если все проверки пройдены
        self.order_model.create(int(client_id), order_date, delivery_date, status, int(bottle_count))
        messagebox.showinfo("Успех", "Заказ добавлен успешно!")
        self.window.destroy()
