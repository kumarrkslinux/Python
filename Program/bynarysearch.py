#!/usr/bin/python3

# It should be in order 

arra = [10,20,40,70,90,100]

search_value = 5

first_value = 0 
end_value = len(arra)-1

while end_value >= first_value:
    mid = first_value + (end_value - first_value)//2
    if arra[mid] == search_value:
        result = mid 
        break 
    elif arra[mid] > search_value:
        end_value = mid -1 

    else:
        first_value = mid +1 
else:
    result = -1

if result != -1: 
    print ("Element is present at Index ", result)
else: 
    print ("Element is not present in Array")
