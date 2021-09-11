#!/usr/bin/python3
sentence = "How are you how is work going on"
number_words = 1

for letter in sentence: 
    if letter == ' ':
        number_words += 1
print ("number of words", number_words)
