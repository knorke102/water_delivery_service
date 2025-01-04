import tkinter as tk
from ui.add_form.add_client_window import AddClientWindow
from ui.show_form.show_client_window import ShowClientWindow

class ClientWindow:
    def __init__(self, parent, client_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление клиентами")
        self.window.geometry("400x200")
        self.client_model = client_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление клиентами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить нового клиента", width=30, command=self.add_client).pack(pady=5)
        tk.Button(self.window, text="Показать всех клиентов", width=30, command=self.show_clients).pack(pady=5)

    def add_client(self):
        AddClientWindow(self.window, self.client_model)

    def show_clients(self):
        ShowClientWindow(self.window, self.client_model)
