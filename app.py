import tkinter as tk

# Импортируем модели
from models.client import Client
from models.order import Order
from models.delivery import Delivery
from models.payment import Payment

# Импортируем интерфейс
from ui.main_form.client_window import ClientWindow
from ui.main_form.order_window import OrderWindow
from ui.main_form.delivery_window import DeliveryWindow
from ui.main_form.payment_window import PaymentWindow


class WaterDeliveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление службой доставки воды")
        self.root.geometry("400x300")

        self.client_model = Client()
        self.order_model = Order()
        self.delivery_model = Delivery()
        self.payment_model = Payment()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Управление службой доставки воды", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Управление клиентами", width=30, command=self.manage_clients).pack(pady=5)
        tk.Button(self.root, text="Управление заказами", width=30, command=self.manage_orders).pack(pady=5)
        tk.Button(self.root, text="Управление доставками", width=30, command=self.manage_deliveries).pack(pady=5)
        tk.Button(self.root, text="Управление платежами", width=30, command=self.manage_payments).pack(pady=5)

    def manage_clients(self):
        ClientWindow(self.root, self.client_model)

    def manage_orders(self):
        OrderWindow(self.root, self.order_model)

    def manage_deliveries(self):
        DeliveryWindow(self.root, self.delivery_model)

    def manage_payments(self):
        PaymentWindow(self.root, self.payment_model)


def run_app():
    root = tk.Tk()
    WaterDeliveryApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
