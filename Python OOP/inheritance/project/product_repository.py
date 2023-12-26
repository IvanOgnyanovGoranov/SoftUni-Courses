from typing import List
from project.product import Product

class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return [p for p in self.products if p.name == product_name][0]

    def remove(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)

    def __repr__(self):
        string = ""
        for st in self.products:
            string += f"{st.name}: {st.quantity}\n"

        return string



