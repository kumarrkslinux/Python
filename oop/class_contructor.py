#!/usr/bin/python3.6

class SuperMarket:
    def __init__ (self, name, price, discount): # its _ _ double time
        self.name  = name
        self.price = price
        self.discount = discount
product1 = SuperMarket('Soap',20,5.0)
product2 = SuperMarket('shampoo',10,2.0)
product3 = SuperMarket('rice',600,10.0)

print(product1.name)
#print(product2.price)
#print(product3.discount)
