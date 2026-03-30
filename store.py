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

    def get_all_products(self) -> List[Product]:
        """get all products that are active"""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """order a new product"""
        total_price = 0

        for product, quantity in shopping_list:
            if product.get_quantity() < quantity:
                raise Exception(f"Not enough stock for {product.name}")

            price = quantity * product.price
            total_price += price

            product.set_quantity(product.get_quantity() - quantity)

        return total_price