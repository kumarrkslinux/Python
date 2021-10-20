#!/usr/bin/python3.9
# Default Arguments 
def find_discount(mrp,perc=10):
    discount = mrp ** (perc/100)
    new_price = mrp - discount
    price(new_price)
    
find_discount(100)
find_discount(100,25)
