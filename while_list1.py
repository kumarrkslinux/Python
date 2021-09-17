#!/usr/bin/python3
new_letters = ['kannan', 'anil', 'sunil', 'madu']
numbers = [33, 22, 55, 66]
both = [new_letters,numbers]
print(both)
match=0
while match < len(both):
      item = 0
      while item < len(both[match]):
          if match == 1 and item == 1 :
             both[match][item] = '44'
          item = item +1
      print()
      match = match +1
print(both)
         
