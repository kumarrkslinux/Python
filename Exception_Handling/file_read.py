#!/usr/bin/python3.6

file = open("file.txt")

print(file.readline(),end=' ')

for line in file:

    print(line, end=' ')

file.close()
