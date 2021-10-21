#!/usr/bin/python3.6
# Default Arguments 
def find_discount(mrp,perc=10):
    discount = mrp ** (perc/100)
    new_price = mrp - discount
    print(new_price)
    
find_discount(100)    # Default value taken 
find_discount(100,25)
