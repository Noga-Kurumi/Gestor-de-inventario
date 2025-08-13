class Product():
    def __init__(self, name, price, description, stock):
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def __str__(self):
        return f"Producto: {self.name}\nPrecio: ${self.price}\nDescripcion: {self.description}\nStock: {self.stock}u."