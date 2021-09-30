#!/usr/bin/python3

Fruits = { 'apple': 100, 'orange': 150, 'redbanana': 80, 'mango': 180 }

for key,value in Fruits.items():
    Fruits[key] = round(value * 1.1, 2 )
    print(Fruits)
