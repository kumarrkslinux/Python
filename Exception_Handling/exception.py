#!/usr/bin/python3.6

# an unexpted even occured that stop the normal flow of a program is known as exception 
#error raised in try block..so alternative solution is given by except block

#1) Exception 
#2) Error vs Exception 
#3) Few Python Built in Exceptions 
#4) Exception Python keywords 
#5) try without except 
#6) try with multiple except 
#7) try except finally 8) Default except

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
######################################################################################
try: 
    x = int(input("Enter no ")) 
    y = int(input("Enter no ")) 
    print(x/y) 

#except (ZeroDivisionError, ValueError) as msg: 
except ZeroDivisionError:
        print("check your value")
except ValueError:
        print("value error")

finally:                                      ########## DB cleaning and connetion closing############
    print("check your finally")
