import tkinter as tk
from ui.add_form.add_payment_window import AddPaymentWindow
from ui.show_form.show_payment_window import ShowPaymentsWindow

class PaymentWindow:
    def __init__(self, parent, payment_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление платежами")
        self.window.geometry("400x200")
        self.payment_model = payment_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление платежами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить новый платеж", width=30, command=self.add_payment).pack(pady=5)
        tk.Button(self.window, text="Показать все платежи", width=30, command=self.show_payments).pack(pady=5)

    def add_payment(self):
        AddPaymentWindow(self.window, self.payment_model)

    def show_payments(self):
        ShowPaymentsWindow(self.window, self.payment_model)
