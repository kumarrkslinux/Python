#!/usr/bin/python3
def find_discount(mrp,perc):
    discount = mrp ** (perc/100)
    new_price = mrp - discount
    print(new_price)
    
find_discount(mrp=100,perc=25)
find_discount(perc=25,mrp=100)
