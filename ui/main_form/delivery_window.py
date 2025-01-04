import tkinter as tk
from ui.add_form.add_delivery_window import AddDeliveryWindow
from ui.show_form.show_delivery_window import ShowDeliveriesWindow

class DeliveryWindow:
    def __init__(self, parent, delivery_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление доставками")
        self.window.geometry("400x200")
        self.delivery_model = delivery_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление доставками", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить новую доставку", width=30, command=self.add_delivery).pack(pady=5)
        tk.Button(self.window, text="Показать все доставки", width=30, command=self.show_deliveries).pack(pady=5)

    def add_delivery(self):
        AddDeliveryWindow(self.window, self.delivery_model)

    def show_deliveries(self):
        ShowDeliveriesWindow(self.window, self.delivery_model)
