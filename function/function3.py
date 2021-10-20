#!/usr/bin/python3

def find_discount(mrp,perc=10):
    discount = mrp ** (perc/100)
    new_price = mrp - discount
    price(new_price)
    
find_discoun(100)
find_discoun(100,25)
