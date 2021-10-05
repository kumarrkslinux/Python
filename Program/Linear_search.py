#!/usr/bin/python3

numbers = [87, 89, 94, 97, 55]

print("linear numbers are: ", numbers)

user_value = int(input("Enter linear number: "))

items = 0

Got_number = False

while items < len(numbers):
    if numbers[items] == user_value:
         Got_number = True
         break 
    items = items +1 

if Got_number == True:
    print("Found number in possition is", items +1 )
else:
    print("Number not found in the list") 
