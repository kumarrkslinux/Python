#!/usr/bin/python3

name1 = { 'madhu', 'arun', 'sudhan'}

name2 = { 'swathi', 'madhu', 'sakthi'}

print(name1 - name2 ) # It should be in first set
print(name1 | name2 ) # eiteher one of the value |union 
print(name1 & name2 ) # Intersection, it will be on both (common in both)
print(name1 ^ name2 ) # (should not be in both set)

#{'arun', 'sudhan'}
#{'sakthi', 'arun', 'swathi', 'sudhan', 'madhu'}
#{'madhu'}
#{'swathi', 'sudhan', 'sakthi', 'arun'}

