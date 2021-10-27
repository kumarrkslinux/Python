#!/usr/bin/python3.6

def get_number():
    number = int(input("Enter your pin: "))
    return number

while True:
    try:
        print(get_number())
        option = input("continue ? yes|no: ")
        if option.lower() == 'no':
            break 
    except:
        print("please enter the valid PIN number")
