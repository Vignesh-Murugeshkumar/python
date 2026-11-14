import csv
from pathlib import Path
class itm:
    payrate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity:int):
        assert price>=0,f"price{price} is not greater than or equal to zero"
        assert quantity>=0,f"quantity{quantity} is not greater than or equal to zero"
        self.name=name
        self.price=price
        self.quantity=quantity
        itm.all.append(self)
    def total_price(self):
        return self.price*self.quantity
    def aply_discount(self):
        self.price*=self.payrate
    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})"
    @property
    def name(self):
        print("getter method called")
        return self.__name
    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception("the name is too long")
        else:
            self.__name=value
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    @price.setter
    def price(self,value):
        if value<0:
            raise Exception("the price is negative")
        else:
            self.__price=value
    @quantity.setter
    def quantity(self,value):
        if value<0:
            raise Exception("the quantity is negative")
        else:
            self.__quantity=value
    def apply_increment(self,increment_value):
        self.price+=self.price*increment_value
    @classmethod
    def instantiate_from_csv(cls):
        with open(Path(__file__).with_name("items.csv"),"r",newline="",encoding="utf-8") as f:
            reader=csv.DictReader(f)
            items=list(reader)
            for item in items:
             cls(
                 name=item['name'],
                price=float(item['price']),
                quantity=int(item['quantity'])
            )
    @staticmethod
    def is_integer(number):
        return isinstance(number,int) or (isinstance(number,float) and number.is_integer())
class phone(itm):
    def __init__(self,name,price,quantity=0,broken_phones=0):
        super().__init__(name,price,quantity)
        assert broken_phones>=0,f"broken phones {broken_phones} is not greater than or equal to zero"
        self.broken_phones=broken_phones

if __name__=="__main__":
    phone1=phone("iphone 17",999.99,10,1)
    phone2=phone("sam",899.99,5,1)
    print(phone1.total_price())
    print(phone2.total_price())
    print(phone1.broken_phones)
    print(phone2.broken_phones)
    print(phone.all)
    print(itm.all)
    item1=itm("laptop",1500,5)
    item1.name="lap"
    print(item1.name)
    item1.quantity=10
    print(item1.quantity)
    phone1.apply_increment(0.1)
    print(phone1.price)