#!/usr/bin/python3
fruits = { 'apple': 100, 'orange': 150, 'redbanana': 80, 'mango': 180 }

for key in list(fruits.keys()):
    if key == 'apple':
        del fruits[key]  # key and value will be deleted 
    print(fruits)
