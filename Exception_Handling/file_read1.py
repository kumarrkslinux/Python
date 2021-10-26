#!/usr/bin/python3.6

file = open("file.txt")
for line in file:
    (city, pincode) = line.split("-")
    print("pincode of ", city, end=' ')
    print('is', pincode, end=' ')

file.close()
