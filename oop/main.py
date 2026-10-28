import csv
from pathlib import Path


class Item:
    pay_rate=0.8 # The pay rate after 20% discount
    all=[] # List to store all instances of the Item class
    def __init__(self, name: str, price: float, quantity: int = 0, has_numpad: bool = True):
        assert price >=0,f"Pricre {price} is not grater than zero equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not grater than zero equal to zero"
        assert isinstance(has_numpad, bool), f"has_numpad {has_numpad} is not a boolean"
        self.name=name
        self.price=price
        self.quantity=quantity
        self.has_numpad=has_numpad
        Item.all.append(self)
    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        csv_path = Path(__file__).with_name('items.csv')
        with csv_path.open('r', newline='', encoding='utf-8') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                quantity=int(item['quantity']),
                has_numpad=bool(item.get('has_numpad'))
            )


Item.instantiate_from_csv()
print(Item.all)