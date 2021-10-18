#!/usr/bin/python3

name = 'kumaraswamy'
CAP = name.capitalize()
print(CAP)

name = 'ANILKUMAR'
CASE = name.casefold()
print(CASE)

name = 'Basic Calulator'
center = name.center(30, '*')
print(center)

sentence = "Learning python is funny. is it correct?"
word="is"
COUNT=sentence.count(word)
print(COUNT)

sentence = "Learning python is funny. is it correct?"
COUNT=sentence.endswith("correct")
print(COUNT)

name = 'xy\tz1\t23\t45\tab\tc'
ex = name.expandtabs(2)
print(ex)

name = 'Is that right way to study python'
fin = name.find("study")
print(fin)

string = "This article is written in {}"
print(string.format("Python"))

new_sentence = "This is new example for the value of work"
output = new_sentence.index("example")
print(output)
