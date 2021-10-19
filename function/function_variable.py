#!/usr/bin/python3

def change(money):
        money = 2000 # local variabe # argument 
        print("change need for", money )

money = 10000 # Global variable 
print ("to be spent", money )

change(money)    # function calling - parameter
print ("remaining amount in hand after change the expected money", money)

