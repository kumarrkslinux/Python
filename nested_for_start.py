#!/usr/bin/python3
word = 'Anbilkannan'
count = len(word)
for number in range(count):
    for letter in range(count):
        print('', end= ' ' )
    for harshvalue in range(number+1):
       print(chr(letter+65), end=' ')
    print()
    count = count -1
