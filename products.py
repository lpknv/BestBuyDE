from helpers import format_currency


class Product:
    active = True

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self):
        self.active = True

    def show(self):
        print(f"{self.name} => Price: {format_currency(self.price)}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        self.quantity -= quantity
        return format_currency(quantity * self.price)