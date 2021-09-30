#!/usr/bin/python3

odd = [1, 3, 5, 7, 9]

even = [2, 4, 6, 8, 10]

print (odd[0])
print (even[-1])
print (odd[:])
print (even[-3:])
print (odd + [11, 13, 15, 17, 19])
even[3] = 18 
print(even)
even.append(21)
print(even)
even.append([23])
print(even)
odd[2:6] = []
print(odd)
