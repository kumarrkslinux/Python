#!/usr/bin/python3
user_input = input("Enter your input: ")
word = user_input[::-1]

if user_input == word:
      print("Its palindrome")
else:
     print("Its not palindrome")
