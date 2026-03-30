from typing import List
from products import Product


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0

        for product, quantity in shopping_list:
            if product.get_quantity() < quantity:
                raise Exception(f"Not enough stock for {product.name}")

            price = quantity * product.price
            total_price += price

            product.set_quantity(product.get_quantity() - quantity)

        return total_price