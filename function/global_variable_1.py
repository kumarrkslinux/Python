#!/usr/bin/python3

x = 10
def loc():
    x = "local"
    print("local x value " , x)

loc()
print("global x value", x)
