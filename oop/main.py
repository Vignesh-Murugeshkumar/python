class Item:
    def __init__(self, name, price, quantity=0, has_numpad=True):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.has_numpad=has_numpad
    def total_price(self):
        return self.price * self.quantity
    

item1=Item("Laptop", 1500, 2)

print("Item 1:", item1.name, item1.price, item1.quantity, item1.total_price())

item2=Item("Smartphone", 800, 3)

item2.price=2000
print("Item 2:", item2.name, item2.price, item2.quantity, item2.total_price())

item2.has_numpad=False