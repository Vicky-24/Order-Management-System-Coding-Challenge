import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dao.i_order_management_repository import IOrderManagementRepository
from entity.user import Userdetails
from entity.product import Product
from util.dbutil import DBUtil
from exception.usernotfound import UserNotFound
from exception.ordernotfound import OrderNotFound
from entity.electronics import Electronics
from entity.clothing import Clothing
class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.db_util = DBUtil()

    def createOrder(self, user: Userdetails, products: list):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            # Insert user if not exists
            cursor.execute("IF NOT EXISTS (SELECT * FROM [Userdetails] WHERE userid = ?) INSERT INTO [Userdetails] (userid, username, password, role) VALUES (?, ?, ?, ?)", 
                           user.userid, user.userid, user.username, user.password, user.role)
            
            # Insert order
            cursor.execute("INSERT INTO [Orders] (userid) OUTPUT INSERTED.orderid VALUES (?)", user.get_userid())
                
            orderid = cursor.fetchone()[0]

            # Insert products for the order
            for product in products:
                # Check current stock for the product
                cursor.execute("SELECT quantityinstock FROM Product WHERE productid = ?", product.productid)
                stock = cursor.fetchone()
                if stock is None:
                    print(f"Product with ID {product.productid} does not exist.")
                    continue
                current_stock = stock[0]
                if product.quantityinstock > current_stock:
                    print(f"Cannot order {product.quantityinstock} units of product {product.productid}. Only {current_stock} units in stock.")
                    continue
                # Insert into OrderProduct
                cursor.execute("INSERT INTO OrderProduct (orderid, productid, quantity) VALUES (?, ?, ?)", orderid, product.productid, product.quantityinstock)
                # Deduct from stock
                new_stock = current_stock - product.quantityinstock
                cursor.execute("UPDATE Product SET quantityinstock = ? WHERE productid = ?", new_stock, product.productid)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def cancelOrder(self, userid: int, orderid: int):
        try:
            connection = DBUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM [Userdetails] WHERE userid = ?", userid)
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    raise UserNotFound(f"User with ID {userid} not found.")

                cursor.execute("SELECT COUNT(*) FROM [Orders] WHERE userid = ? AND orderid = ?", userid, orderid)
                order_count = cursor.fetchone()[0]
                if order_count == 0:
                    raise OrderNotFound(f"Order with ID {orderid} not found for user {userid}.")
                cursor.execute("DELETE FROM OrderProduct WHERE orderid = ?", orderid)
                cursor.execute("DELETE FROM [Orders] WHERE userid = ? AND orderid = ?", userid, orderid)
                connection.commit()
                print("Order cancelled successfully.")
            else:
                print("Failed to connect to database.")
        except UserNotFound as e:
            print("Error :", e)
        except OrderNotFound as e:
            print("Error :", e)
        except Exception as e:
            print("Error :", e)
        finally:
            if connection:
                connection.close()

    def createProduct(self, user: Userdetails, product: Product, electronics:Electronics, clothing: Clothing):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            # Check if the user is admin
            if user.role != "Admin":
                print("Only admin users can create products.")
                return False
            
            cursor.execute("INSERT INTO Product (productid, productname, description, price, quantityinstock, type) VALUES (?, ?, ?, ?, ?, ?)", 
                           product.productid, product.productname, product.description, product.price, product.quantityinstock, product.type)
            if product.type=="Electronics" and electronics is not None:
                cursor.execute("INSERT INTO Electronics (productId, brand, warrantyperiod) VALUES (?, ?, ?)",
                               product.productid, electronics.brand, electronics.warrantyperiod)
            elif product.type == "Clothing" and clothing is not None:
                cursor.execute("INSERT INTO Clothing (productId, size, color) VALUES (?, ?, ?)",
                               product.productid, clothing.size, clothing.color)
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def createUser(self, user: Userdetails):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO [Userdetails] (userid, username, password, role) VALUES (?, ?, ?, ?)", user.userid, user.username, user.password, user.role)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def getAllProducts(self):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Product")
            products = cursor.fetchall()
            conn.close()
            return products
        except Exception as e:
            print("Error:", e)
            return None

    def getOrderByUser(self, user: Userdetails):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            # Query to retrieve order details including product name and quantity bought
            query = """
            SELECT o.orderId, p.productName, op.quantity
            FROM [Orders] o
            JOIN OrderProduct op ON o.orderid = op.orderid
            JOIN Product p ON op.productid = p.productid
            WHERE o.userid = ?
            """

            cursor.execute(query, user.userid)
            orders = cursor.fetchall()
            conn.close()
            return orders
        except Exception as e:
            print("Error:", e)
            return None
    