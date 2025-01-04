import tkinter as tk
from tkinter import ttk
from collections import Counter
from tkinter import messagebox

class ShowDeliveriesWindow:
    def __init__(self, parent, delivery_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список доставок")
        self.delivery_model = delivery_model
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.window, text="Список доставок", font=("Arial", 14)).pack(pady=10)

        # Выбор отображаемых колонок
        self.column_choices = {
            "ID Доставки": tk.BooleanVar(value=True),
            "ID Заказа": tk.BooleanVar(value=True),
            "Дата доставки": tk.BooleanVar(value=True),
            "Статус доставки": tk.BooleanVar(value=True),
            "Имя водителя": tk.BooleanVar(value=True),
            "Номер транспорта": tk.BooleanVar(value=True),
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

        tk.Label(filter_frame, text="Поиск по статусу или имени водителя:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_deliveries)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_driver_button = tk.Button(filter_frame, text="Сортировать по имени водителя",
                                            command=lambda: self.sort_deliveries("Имя водителя"))
        self.sort_driver_button.pack(side=tk.LEFT, padx=5)

        # Кнопка для определения самого частого курьера
        self.most_frequent_driver_button = tk.Button(self.window, text="Курьер с наибольшим числом доставок",
                                                     command=self.show_most_frequent_driver)
        self.most_frequent_driver_button.pack(pady=5)

        # Загружаем все данные
        self.load_data()

    def load_data(self, filter_text=None, deliveries=None):
        if not deliveries:
            deliveries = self.delivery_model.get_all()

        if filter_text:
            deliveries = [
                delivery for delivery in deliveries
                if filter_text.lower() in delivery[3].lower() or filter_text.lower() in delivery[4].lower()
            ]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for delivery in deliveries:
            values = []
            if "ID Доставки" in selected_columns:
                values.append(delivery[0])
            if "ID Заказа" in selected_columns:
                values.append(delivery[1])
            if "Дата доставки" in selected_columns:
                values.append(delivery[2])
            if "Статус доставки" in selected_columns:
                values.append(delivery[3])
            if "Имя водителя" in selected_columns:
                values.append(delivery[4])
            if "Номер транспорта" in selected_columns:
                values.append(delivery[5])

            self.tree.insert("", "end", values=values)

    def search_deliveries(self):
        search_text = self.search_entry.get()
        self.load_data(filter_text=search_text)

    def sort_deliveries(self, column):
        deliveries = self.delivery_model.get_all()

        if column == "Имя водителя":
            deliveries.sort(key=lambda delivery: delivery[4].lower())

        self.load_data(deliveries=deliveries)

    def update_columns(self):
        self.load_data()

    def show_most_frequent_driver(self):
        # Получаем все доставки из модели
        deliveries = self.delivery_model.get_all()

        # Считаем количество доставок для каждого водителя
        driver_counts = Counter([delivery[4] for delivery in deliveries])

        # Определяем курьера с наибольшим числом доставок
        if driver_counts:
            most_frequent_driver, count = driver_counts.most_common(1)[0]
            message = f"Курьер с наибольшим числом доставок: {most_frequent_driver} ({count} раз)"
        else:
            message = "Доставки не найдены."

        # Отображаем результат
        messagebox.showinfo("Результат", message)
