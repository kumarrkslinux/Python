#!/usr/bin/python3
kannan = { 10,20,30,40 }
new_kannan = frozenset(kannan)
new_kannan.append(50)
print(new_kannan)
#AttributeError: 'frozenset' object has no attribute 'append'
