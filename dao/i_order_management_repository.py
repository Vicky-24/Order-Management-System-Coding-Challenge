import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from entity.user import Userdetails
from entity.product import Product

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: Userdetails, products: list):
        pass

    @abstractmethod
    def cancelOrder(self, userId: int, orderId: int):
        pass

    @abstractmethod
    def createProduct(self, user: Userdetails, product: Product):
        pass

    @abstractmethod
    def createUser(self, user: Userdetails):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, user: Userdetails):
        pass