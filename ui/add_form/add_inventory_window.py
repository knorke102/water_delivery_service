import tkinter as tk
from tkinter import messagebox

class AddInventoryWindow:
    def __init__(self, parent, inventory_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить товар")
        self.inventory_model = inventory_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о товаре", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Название товара").pack()
        self.item_name_entry = tk.Entry(self.window)
        self.item_name_entry.pack(pady=5)

        tk.Label(self.window, text="Описание товара").pack()
        self.item_description_entry = tk.Entry(self.window)
        self.item_description_entry.pack(pady=5)

        tk.Label(self.window, text="Количество на складе").pack()
        self.stock_quantity_entry = tk.Entry(self.window)
        self.stock_quantity_entry.pack(pady=5)

        tk.Label(self.window, text="Цена за единицу").pack()
        self.unit_price_entry = tk.Entry(self.window)
        self.unit_price_entry.pack(pady=5)

        tk.Button(self.window, text="Добавить товар", width=30, command=self.add_item).pack(pady=10)

    def add_item(self):
        item_name = self.item_name_entry.get()
        item_description = self.item_description_entry.get()
        stock_quantity = self.stock_quantity_entry.get()
        unit_price = self.unit_price_entry.get()

        # Проверка корректности данных
        if not item_name or not item_description or not stock_quantity or not unit_price:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        # Проверка количества на складе (должно быть целым числом >= 0)
        if not stock_quantity.isdigit() or int(stock_quantity) < 0:
            messagebox.showerror("Ошибка", "Количество на складе должно быть неотрицательным целым числом!")
            return

        # Проверка цены за единицу (должна быть числом > 0)
        try:
            unit_price = float(unit_price)
            if unit_price <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Цена за единицу должна быть положительным числом!")
            return

        # Если все проверки пройдены, добавляем товар
        self.inventory_model.create(item_name, item_description, int(stock_quantity), unit_price)
        messagebox.showinfo("Успех", "Товар добавлен успешно!")
        self.window.destroy()
