import re
import tkinter as tk
from tkinter import messagebox

class AddClientWindow:
    def __init__(self, parent, client_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить клиента")
        self.client_model = client_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о клиенте", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Имя").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Адрес").pack()
        self.address_entry = tk.Entry(self.window)
        self.address_entry.pack(pady=5)

        tk.Label(self.window, text="Телефон").pack()
        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.pack(pady=5)

        tk.Label(self.window, text="Электронная почта").pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack(pady=5)

        tk.Button(self.window, text="Добавить клиента", width=30, command=self.add_client).pack(pady=10)

    def add_client(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Проверка корректности данных
        if not name or not address or not phone or not email:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        # Проверка имени (должно содержать только буквы)
        if not name.isalpha():
            messagebox.showerror("Ошибка", "Имя должно содержать только буквы!")
            return

        # Проверка адреса (должен быть хотя бы 5 символов)
        if len(address) < 5:
            messagebox.showerror("Ошибка", "Адрес должен содержать хотя бы 5 символов!")
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

        # Если все проверки пройдены, добавляем клиента
        self.client_model.create(name, address, phone, email)
        messagebox.showinfo("Успех", "Клиент добавлен успешно!")
        self.window.destroy()
