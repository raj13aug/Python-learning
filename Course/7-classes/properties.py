class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value

    price = property(get_price, set_price)

# A property is an object that sits in front of an attribute and allows us to get or set the value of an attribute.
# We want them to have minimal number of function or method exposed to outside.


product = Product(50)
print(product.price)

# We used a decorator called class method convert an instance method and class a class method.we have another decorator creating a property,


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value


product = Product(10)
print(product.price)
