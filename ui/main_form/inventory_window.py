import tkinter as tk
from ui.add_form.add_inventory_window import AddInventoryWindow
from ui.show_form.show_inventory_window import ShowInventoryWindow

class InventoryWindow:
    def __init__(self, parent, inventory_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление товарами")
        self.window.geometry("400x200")
        self.inventory_model = inventory_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление товарами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить новый товар", width=30, command=self.add_item).pack(pady=5)
        tk.Button(self.window, text="Показать все товары", width=30, command=self.show_items).pack(pady=5)

    def add_item(self):
        AddInventoryWindow(self.window, self.inventory_model)

    def show_items(self):
        ShowInventoryWindow(self.window, self.inventory_model)
