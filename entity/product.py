class Product:
    def __init__(self, productid, productname, description, price, quantityinstock, type):
        self.productid = productid
        self.productname = productname
        self.description = description
        self.price = price
        self.quantityinstock = quantityinstock
        self.type = type

    # Getters
    def get_productid(self):
        return self.productid

    def get_productname(self):
        return self.productname

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantityinstock(self):
        return self.quantityinstock

    def get_type(self):
        return self.type

    # Setters
    def set_productid(self, productid):
        self.productid = productid

    def set_productname(self, productname):
        self.productname = productname

    def set_description(self, description):
        self.description = description

    def set_price(self, price):
        self.price = price

    def set_quantityinstock(self, quantityinstock):
        self.quantityinstock = quantityinstock

    def set_type(self, type):
        self.type = type
