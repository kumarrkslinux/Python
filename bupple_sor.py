#!/usr/bin/python3
array = [ 2,4,6,8,7,9,3,5,1 ]

length = len(array)-1
for j in range(length):
    for i in range(0,length):
        if array[i] > array[i+1]:
           array[i],array[i+1] = array[i+1],array[i]
length = length -1
print(array)
