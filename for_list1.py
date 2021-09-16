#!/usr/bin/python3
odd1 = [1, 3, 5, 7, 9]

string1 = ['a', 'b', 'c', 'd', 'e']

both = [ odd1, string1]

for list in both:
   for innerlist in list:
#       print(type(innerlist))
        if type(innerlist) == str and innerlist.isalpha ():
           print(innerlist, end=' ')
print()
