#!/usr/bin/python3

def sum(num1, num2): 
    return num1 + num2 
result = sum(5,10) 
print(result)


def palindrome(sentence):
    return sentence == sentence[::-1]
 
sensence = input("Enter one word: ")
if palindrome(sensence):
    print("its palindrome word")
else: 
    print("it is not palindrome word")
