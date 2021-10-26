#!/usr/bin/python3.6

# an unexpted even occured that stop the normal flow of a program is known as exception 
#error raised in try block..so alternative solution is given by except block
x = int(input('Enter no ')) 
y = int(input('Enter no ')) 
print(x/y)

try: 
    print(10/0) 
except ZeroDivisionError as msg: 
    print(type(msg))

try: 
    print(10/0) 
except ZeroDivisionError: 
    print(100/5)

try: 
    x = int(input("Enter no ")) 
    y = int(input("Enter no ")) 
    print(x/y) 
except (ZeroDivisionError, ValueError) as msg: 
    print(msg)
