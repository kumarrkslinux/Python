#!/usr/bin/python3
mark = { 'kannan': 86, 'sudhan': 80 }

print (mark)

mark['sudhan'] = 88

print(mark)

mark['anbuselvan'] = 98

print(mark)

del mark['kannan']

print(mark)

LIST=list(mark)

TUPLE=tuple(mark)

SET=set(mark)

KEYS=mark.keys()

VALUE=mark.values()

ONLY_VALUE=[*mark.values()]

ONLY_KEY=[*mark.keys()]

ONLY_VALUE1=[(88, 98)]

print(LIST)

print(SET)

print(TUPLE)

print(KEYS)

print(VALUE)

print(ONLY_VALUE)

print(ONLY_KEY)

print(ONLY_VALUE1)
