#!/usr/bin/python3
range1 = range(10)
range2 = range(20,40)
range3 = range(20, 5,-2)
range4 = range(5,20 ,2)

for a in range1:
    print(a)

print()

for b in range2:
    print(b, end=' ')
print()

for c in range3:
    print(c, end=' ')
print()

print(range4[4])
print(range4[2:5])
print(range4[-1])
