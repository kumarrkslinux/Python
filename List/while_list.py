#!/usr/bin/python3
letters = ['anbu', 'arun', 'madu', 'guru']
number = [6, 9, 8, 3]
both = [letters, number]
print(both)
mach=0
while mach < len(both):
      item = 0
      while item < len(both[mach]):
        if (type(both[mach][item]) == int ): 
#        if (type(both[mach][item]) == str ): 
           print(both[mach][item], end=' ')
        item = item +1 
      print()
      mach = mach + 1
    
