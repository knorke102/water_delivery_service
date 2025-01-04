import re
import tkinter as tk
from tkinter import ttk, messagebox

class AddPaymentWindow:
    def __init__(self, parent, payment_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить платеж")
        self.payment_model = payment_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о платеже", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="ID заказа").pack()
        self.order_id_entry = tk.Entry(self.window)
        self.order_id_entry.pack(pady=5)

        tk.Label(self.window, text="Дата платежа").pack()
        self.payment_date_entry = tk.Entry(self.window)
        self.payment_date_entry.pack(pady=5)

        tk.Label(self.window, text="Сумма платежа").pack()
        self.payment_amount_entry = tk.Entry(self.window)
        self.payment_amount_entry.pack(pady=5)

        tk.Label(self.window, text="Метод платежа").pack()
        self.payment_method_entry = ttk.Combobox(self.window, values=["Карта", "Наличные"], state="readonly")
        self.payment_method_entry.pack(pady=5)
        self.payment_method_entry.set("Карта")

        tk.Button(self.window, text="Добавить платеж", width=30, command=self.add_payment).pack(pady=10)

    def add_payment(self):
        order_id = self.order_id_entry.get()
        payment_date = self.payment_date_entry.get()
        payment_amount = self.payment_amount_entry.get()
        payment_method = self.payment_method_entry.get()

        # Проверка корректности данных
        if not order_id or not payment_date or not payment_amount or not payment_method:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        # Проверка ID заказа
        if not payment_amount.isdigit():
            messagebox.showerror("Ошибка", "ID заказа должно быть числом!")
            return

        # Проверка суммы заказа
        if not payment_amount.isdigit():
            messagebox.showerror("Ошибка", "Сумма платежа должно быть числом!")
            return

        # Проверка формата даты (например, "YYYY-MM-DD")
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, payment_date):
            messagebox.showerror("Ошибка", "Неверный формат даты! Используйте формат: YYYY-MM-DD")
            return

        # Если все проверки пройдены, добавляем платеж
        self.payment_model.create(int(order_id), payment_date, payment_amount, payment_method)
        messagebox.showinfo("Успех", "Платеж добавлен успешно!")
        self.window.destroy()
