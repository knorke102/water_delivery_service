import tkinter as tk
from tkinter import ttk

class ShowInventoryWindow:
    def __init__(self, parent, inventory_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список товаров")
        self.inventory_model = inventory_model
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.window, text="Список товаров", font=("Arial", 14)).pack(pady=10)

        # Выбор отображаемых колонок
        self.column_choices = {
            "ID": tk.BooleanVar(value=True),
            "Название": tk.BooleanVar(value=True),
            "Описание": tk.BooleanVar(value=True),
            "Количество": tk.BooleanVar(value=True),
            "Цена за единицу": tk.BooleanVar(value=True),
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

        tk.Label(filter_frame, text="Поиск по названию или описанию:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_inventory)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_name_button = tk.Button(filter_frame, text="Сортировать по названию",
                                          command=lambda: self.sort_inventory("name"))
        self.sort_name_button.pack(side=tk.LEFT, padx=5)

        # Загружаем все данные
        self.load_data()

    def load_data(self, filter_text=None, items=None):
        if not items:
            items = self.inventory_model.get_all()

        if filter_text:
            items = [item for item in items if
                     filter_text.lower() in item[1].lower() or filter_text.lower() in item[2].lower()]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for item in items:
            values = []
            if "ID" in selected_columns:
                values.append(item[0])
            if "Название" in selected_columns:
                values.append(item[1])
            if "Описание" in selected_columns:
                values.append(item[2])
            if "Количество" in selected_columns:
                values.append(item[3])
            if "Цена за единицу" in selected_columns:
                values.append(item[4])

            self.tree.insert("", "end", values=values)

    def search_inventory(self):
        search_text = self.search_entry.get()
        self.load_data(filter_text=search_text)

    def sort_inventory(self, column):
        items = self.inventory_model.get_all()

        if column == "name":
            items.sort(key=lambda item: item[1].lower())

        self.load_data(items=items)

    def update_columns(self):
        self.load_data()
