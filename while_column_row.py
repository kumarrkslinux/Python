#!/usr/bin/python3
row = 1

while row <= 5:
     column = 1
     value = 65
     while column <= row :
         print(chr(value), end='')
         value = value + 1 
         column = column + 1
     print()
     row = row +1 
