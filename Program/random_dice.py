#!/usr/bin/python3

from random import randint

min_value = 1
max_value = 10

again = True

while again:
    print("Dice role value: ", randint(min_value, max_value))
    role_again = input("please press 'Y' again if you want to roll again: ")
    if role_again.lower() == 'yes' or role_again.lower() == 'y':
        again = True
    else:
       again = False
