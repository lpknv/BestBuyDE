from helpers import format_currency


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.formatted_price = format_currency(self.price)

    def get_quantity(self) -> int:
        """get product quantity"""
        return self.quantity

    def set_quantity(self, quantity):
        """set product quantity"""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """check if a product is active"""
        return self.active

    def activate(self) -> None:
        """activate a product"""
        self.active = True

    def deactivate(self) -> None:
        """deactivate a product"""
        self.active = False

    def show(self):
        """print all information about a product"""
        print(f"{self.name} => Price: {format_currency(self.price)}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """buy a product and return the total price"""
        if not self.active:
            raise Exception(f"{self.name} is not active")

        if quantity > self.quantity:
            raise Exception(f"Not enough stock for {self.name}")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price