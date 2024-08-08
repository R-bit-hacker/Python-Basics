class Order:
    def __init__(self, item, price):
        self.item=item
        self.price=price

    def __gt__(self,o2):
        return self.price > o2.price



o1=Order("soap", 130)
o2=Order("shampoo",450)
print(o1>o2)