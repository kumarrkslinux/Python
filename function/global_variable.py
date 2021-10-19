#!/usr/bin/python3
#price = 10
#def sell():
#    price = price + 20
#    print(price)
#sell()

price = 10
def sell():
    global price
    price = price + 20
    print(price)
sell()
print(price)
