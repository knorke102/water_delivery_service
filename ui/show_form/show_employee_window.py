import tkinter as tk
from tkinter import ttk

class ShowEmployeeWindow:
    def __init__(self, parent, employee_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список сотрудников")
        self.employee_model = employee_model
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.window, text="Список сотрудников", font=("Arial", 14)).pack(pady=10)

        # Выбор отображаемых колонок
        self.column_choices = {
            "ID": tk.BooleanVar(value=True),
            "Имя": tk.BooleanVar(value=True),
            "Должность": tk.BooleanVar(value=True),
            "Телефон": tk.BooleanVar(value=True),
            "Электронная почта": tk.BooleanVar(value=True),
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

        tk.Label(filter_frame, text="Поиск по имени или телефону:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_employees)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_name_button = tk.Button(filter_frame, text="Сортировать по имени",
                                          command=lambda: self.sort_employees("name"))
        self.sort_name_button.pack(side=tk.LEFT, padx=5)

        # Загружаем все данные
        self.load_data()

    def load_data(self, filter_text=None, employees=None):
        if not employees:
            employees = self.employee_model.get_all()

        if filter_text:
            employees = [employee for employee in employees if
                         filter_text.lower() in employee[1].lower() or filter_text.lower() in employee[3].lower()]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for employee in employees:
            values = []
            if "ID" in selected_columns:
                values.append(employee[0])
            if "Имя" in selected_columns:
                values.append(employee[1])
            if "Должность" in selected_columns:
                values.append(employee[2])
            if "Телефон" in selected_columns:
                values.append(employee[3])
            if "Электронная почта" in selected_columns:
                values.append(employee[4])

            self.tree.insert("", "end", values=values)

    def search_employees(self):
        search_text = self.search_entry.get()
        self.load_data(filter_text=search_text)

    def sort_employees(self, column):
        employees = self.employee_model.get_all()

        if column == "name":
            employees.sort(key=lambda employee: employee[1].lower())

        self.load_data(employees=employees)

    def update_columns(self):
        self.load_data()
