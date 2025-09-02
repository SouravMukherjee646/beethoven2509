# id, name, description, category, tags, stock, price
class Product:
    def __init__(self, id, name, description, category, tags, stock, price):  #arguments & attributes
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price
    def __str__(self):
        return f'[id = {self.id}, name = {self.name}, description = {self.description}, category = {self.category}, tags = {self.tags}, stock = {self.stock}, price = {self.price}]'
    def __repr__(self):
        return self.__str__()
   
mobile_oneplus = Product(1001, 'Oneplus Nord CE5', 'Good Battery, 8+256GB', 'Phone', 'Smartphone, 5G', 10, 26999)
print(mobile_oneplus)

mobile_oneplus2 = Product(1002, description = 'Good Battery, 6+128GB', name = 'Oneplus Nord CE5', tags = 'Smartphone, 5G', stock = 10, category = 'Phone', price = 24999)
print(mobile_oneplus2)