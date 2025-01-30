import tkinter as tk
from ui.add_form.add_employee_window import AddEmployeeWindow
from ui.show_form.show_employee_window import ShowEmployeeWindow

class EmployeeWindow:
    def __init__(self, parent, employee_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление сотрудниками")
        self.window.geometry("400x200")
        self.employee_model = employee_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление сотрудниками", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить нового сотрудника", width=30, command=self.add_employee).pack(pady=5)
        tk.Button(self.window, text="Показать всех сотрудников", width=30, command=self.show_employees).pack(pady=5)

    def add_employee(self):
        AddEmployeeWindow(self.window, self.employee_model)

    def show_employees(self):
        ShowEmployeeWindow(self.window, self.employee_model)
