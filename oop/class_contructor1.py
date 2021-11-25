#!/usr/bin/python3.6
class SuperMarket:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def product_details(self):
         #return '{} - {} - #{}'.format(self.name,self.price,self.discount) # space holder 
         #return '{}/{}/{}'.format('19','Nov', '2021') # space replacement oberator
         # 09/Nov/2021
         return self.name, self.price, self.discount

product1 = SuperMarket('Soap',20,5.0)
product2 = SuperMarket('shampoo',10,2.0)
product3 = SuperMarket('rice',600,10.0)

print(product1.product_details()) # Method Calling Statement 
print(product2.product_details()) 
print(SuperMarket.product_details(product1))
