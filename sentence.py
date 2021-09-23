#!/usr/bin/python3

total_sentence= " Love is god"

for word in total_sentence:
     length = leg(word)
     number = 0
       while word < length:
             if word in [a,e,i,o,u]:
                number = number +1 
                print(word, end='')
print()
