#!/usr/bin/python3
def mrp(sellingprice,buyingprice,**tax):
    print(sellingprice)
    print(buyingprice)
    for key,value in tax.items():
        print('%s = %s'%(key, value) )
        print(key, type(key))
        print(value, type(value))

mrp(100,90,sgst=5,cgst=6)
