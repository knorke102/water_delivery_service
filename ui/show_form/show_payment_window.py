import tkinter as tk
from tkinter import ttk

class ShowPaymentsWindow:
    def __init__(self, parent, payment_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список платежей")
        self.payment_model = payment_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Список платежей", font=("Arial", 14)).pack(pady=10)

        # Выбор отображаемых колонок
        self.column_choices = {
            "ID Платежа": tk.BooleanVar(value=True),
            "ID Заказа": tk.BooleanVar(value=True),
            "Дата платежа": tk.BooleanVar(value=True),
            "Сумма платежа": tk.BooleanVar(value=True),
            "Метод платежа": tk.BooleanVar(value=True),
        }

        tk.Label(self.window, text="Выберите отображаемые колонки:").pack(pady=5)

        columns_frame = tk.Frame(self.window)
        columns_frame.pack(pady=5)

        for col, var in self.column_choices.items():
            tk.Checkbutton(columns_frame, text=col, variable=var, command=self.update_columns).pack(side=tk.LEFT, padx=5)

        # Таблица
        self.tree = ttk.Treeview(self.window, show="headings", height=10)
        self.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Фильтрация/Поиск и Сортировка
        filter_frame = tk.Frame(self.window)
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Поиск по методу платежа или ID заказа:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_payments)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_button = tk.Button(filter_frame, text="Сортировать по методу платежа", command=lambda: self.sort_payments("Метод платежа"))
        self.sort_button.pack(side=tk.LEFT, padx=5)

        # Загружаем все данные
        self.load_data()

    def load_data(self, filter_text=None, payments=None):
        if not payments:
            payments = self.payment_model.get_all()

        if filter_text:
            payments = [
                payment for payment in payments
                if filter_text.lower() in str(payment[4]).lower() or filter_text.lower() in str(payment[1]).lower()
            ]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for payment in payments:
            values = []
            if "ID Платежа" in selected_columns:
                values.append(payment[0])
            if "ID Заказа" in selected_columns:
                values.append(payment[1])
            if "Дата платежа" in selected_columns:
                values.append(payment[2])
            if "Сумма платежа" in selected_columns:
                values.append(payment[3])
            if "Метод платежа" in selected_columns:
                values.append(payment[4])

            self.tree.insert("", "end", values=values)

    def search_payments(self):
        search_text = self.search_entry.get()
        self.load_data(filter_text=search_text)

    def sort_payments(self, column):
        payments = self.payment_model.get_all()

        if column == "Метод платежа":
            payments.sort(key=lambda payment: payment[4].lower())

        self.load_data(payments=payments)

    def update_columns(self):
        self.load_data()
