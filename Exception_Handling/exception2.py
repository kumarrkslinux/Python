#!/usr/bin/python3.6

try:
    file = open("file.txt")
    for line in file:
        try:        
            (city, pincode) = line.split("-")
            print("pincode of ", city, end=' ')
            print('is', pincode, end=' ')
        except: 
              pass

    file.close()

except: 
    print("please check your file")
