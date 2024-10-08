import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from entity.product import Product
class Clothing(Product):
    def __init__(self, productid, productname, description, price, quantityinstock, size, color):
        super().__init__(productid, productname, description, price, quantityinstock,"Clothing")
        self.size = size
        self.color = color

    # Getters
    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    # Setters
    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color
