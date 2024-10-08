import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from entity.product import Product
class Electronics(Product):
    def __init__(self, productid, productname, description, price, quantityinstock,brand, warrantyperiod):
        super().__init__(productid, productname, description, price, quantityinstock,"Electronics")
        self.brand = brand
        self.warrantyperiod = warrantyperiod

    # Getters
    def get_brand(self):
        return self.brand

    def get_warrantyperiod(self):
        return self.warrantyperiod

    # Setters
    def set_brand(self, brand):
        self.brand = brand

    def set_warrantyperiod(self, warrantyperiod):
        self.warrantyperiod = warrantyperiod
