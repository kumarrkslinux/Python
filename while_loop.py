#!/usr/bin/python3
thought = 10
match_not_found = True
while match_not_found == True:
    deduction = int(input("Enter your thought number between 1 to 20 "))
    if deduction == thought:
       print("your mind or our thought number is correct", thought) 
       match_not_found = False
       break
    elif deduction >= thought:
       print(" Thought is grater than expected " )
    else:
        print(" Thought is lesser than expected " )
