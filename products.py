from helpers import format_currency


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def show(self):
        print(f"{self.name} => Price: {format_currency(self.price)}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception(f"{self.name} is not active")

        if quantity > self.quantity:
            raise Exception(f"Not enough stock for {self.name}")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price