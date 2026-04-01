from typing import List
from products import Product


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """Add product to product list"""
        self.products.append(product)

    def remove_product(self, product):
        """remove product from product list"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """get total product quantity"""
        return sum(product.get_quantity() for product in self.products)

    def all_active_products(self) -> int:
        """get total quantity of all active products"""
        return sum(
            product.get_quantity()
            for product in self.products
            if product.is_active()
        )

    def get_all_products(self) -> List[Product]:
        """get all active products"""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """order products from the shopping list"""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
