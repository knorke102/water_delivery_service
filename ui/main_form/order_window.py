import tkinter as tk
from ui.add_form.add_order_window import AddOrderWindow
from ui.show_form.show_order_window import ShowOrderWindow

class OrderWindow:
    def __init__(self, parent, order_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление заказами")
        self.window.geometry("400x200")
        self.order_model = order_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление заказами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить новый заказ", width=30, command=self.add_order).pack(pady=5)
        tk.Button(self.window, text="Показать все заказы", width=30, command=self.show_orders).pack(pady=5)

    def add_order(self):
        AddOrderWindow(self.window, self.order_model)

    def show_orders(self):
        ShowOrderWindow(self.window, self.order_model)
