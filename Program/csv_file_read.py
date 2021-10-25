#!/usr/bin/python3.6

import csv
# f -> plate --> python object

# object = Real time Entity - state(structure), abd behavior)

#things =  laptop, mobile, etc

f = open("student.csv", 'r')

w = csv.writer(f)
r = csv.reader(f) # <_csv.reader object at 0x7f68d1579f98>

print(r)

data = list(r) # type casting 
print(data)

#for row in data:
#    print(row)
