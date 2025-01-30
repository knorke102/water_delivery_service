import re
import tkinter as tk
from tkinter import messagebox

class AddEmployeeWindow:
    def __init__(self, parent, employee_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить сотрудника")
        self.employee_model = employee_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о сотруднике", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Имя сотрудника").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Должность").pack()
        self.role_entry = tk.Entry(self.window)
        self.role_entry.pack(pady=5)

        tk.Label(self.window, text="Телефон").pack()
        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.pack(pady=5)

        tk.Label(self.window, text="Электронная почта").pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack(pady=5)

        tk.Label(self.window, text="Дата найма").pack()
        self.hire_date_entry = tk.Entry(self.window)
        self.hire_date_entry.pack(pady=5)

        tk.Button(self.window, text="Добавить сотрудника", width=30, command=self.add_employee).pack(pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        role = self.role_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        hire_date = self.hire_date_entry.get()

        # Проверка корректности данных
        if not name or not role or not phone or not email or not hire_date:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        # Проверка имени (должно содержать только буквы и пробелы)
        if not all(part.isalpha() for part in name.split()):
            messagebox.showerror("Ошибка", "Имя должно содержать только буквы!")
            return

        # Проверка формата телефона (например, +7 xxx xxx-xx-xx)
        phone_pattern = r"^\+7\s\d{3}\s\d{3}-\d{2}-\d{2}$"
        if not re.match(phone_pattern, phone):
            messagebox.showerror("Ошибка", "Неверный формат телефона! Используйте формат: +7 xxx xxx-xx-xx")
            return

        # Проверка формата email
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            messagebox.showerror("Ошибка", "Неверный формат email!")
            return

        # Проверка формата даты найма (ГГГГ-ММ-ДД)
        hire_date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(hire_date_pattern, hire_date):
            messagebox.showerror("Ошибка", "Дата найма должна быть в формате ГГГГ-ММ-ДД!")
            return

        # Если все проверки пройдены, добавляем сотрудника
        self.employee_model.create(name, role, phone, email, hire_date)
        messagebox.showinfo("Успех", "Сотрудник добавлен успешно!")
        self.window.destroy()
