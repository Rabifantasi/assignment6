# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, 
# and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


p = Product(1000)
print("Current price:", p.price)

p.price = 1500
print("Updated price:", p.price)

del p.price

