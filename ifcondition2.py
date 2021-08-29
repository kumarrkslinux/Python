#!/usr/bin/python3
age = int(input("Enter your age: "))

if age > 5:
     nationality = input("Enter your nationality: ")
     if nationality == 'INDIAN':
        print ("elgible for aadhar")
     else:
        print ("Not for other nationality") 
else:
   print("Age criteria not met")
