import tkinter as tk
from tkinter import ttk

class ShowOrderWindow:
    def __init__(self, parent, order_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список заказов")
        self.order_model = order_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Список заказов", font=("Arial", 14)).pack(pady=10)

        # Выбор отображаемых колонок
        self.column_choices = {
            "ID Заказа": tk.BooleanVar(value=True),
            "ID Клиента": tk.BooleanVar(value=True),
            "Дата Заказа": tk.BooleanVar(value=True),
            "Дата Доставки": tk.BooleanVar(value=True),
            "Статус": tk.BooleanVar(value=True),
            "Кол-во Бутылей": tk.BooleanVar(value=True),
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

        tk.Label(filter_frame, text="Поиск по статусу или ID клиента:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_orders)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_button = tk.Button(filter_frame, text="Сортировать по статусу", command=lambda: self.sort_orders("Статус"))
        self.sort_button.pack(side=tk.LEFT, padx=5)

        # Загружаем все данные
        self.load_data()

    def load_data(self, filter_text=None, orders=None):
        if not orders:
            orders = self.order_model.get_all()

        if filter_text:
            orders = [
                order for order in orders
                if filter_text.lower() in str(order[4]).lower() or filter_text.lower() in str(order[1]).lower()
            ]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for order in orders:
            values = []
            if "ID Заказа" in selected_columns:
                values.append(order[0])
            if "ID Клиента" in selected_columns:
                values.append(order[1])
            if "Дата Заказа" in selected_columns:
                values.append(order[2])
            if "Дата Доставки" in selected_columns:
                values.append(order[3])
            if "Статус" in selected_columns:
                values.append(order[4])
            if "Кол-во Бутылей" in selected_columns:
                values.append(order[5])

            self.tree.insert("", "end", values=values)

    def search_orders(self):
        search_text = self.search_entry.get()
        self.load_data(filter_text=search_text)

    def sort_orders(self, column):
        orders = self.order_model.get_all()

        if column == "Статус":
            orders.sort(key=lambda order: order[4].lower())

        self.load_data(orders=orders)

    def update_columns(self):
        self.load_data()
