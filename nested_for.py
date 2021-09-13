#!/usr/bin/python3
word = 'Anbilkannan'
count = len(word)
for number in range(count):
    for letter in range(count):
        print(chr(letter+65), end= ' ' )
    print()
    count = count -1
