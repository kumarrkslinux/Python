#!/usr/bin/python3

import os 

fname = input("Enter file name with location: ") 


if os.path.isfile(fname): 
    lcount = wcount = ccount = 0 

    print("File is Present") 
    f=open(fname,'r') 
    for line in f:
        lcount = lcount + 1

        words = line.split()
        wcount = wcount + len(words)
        ccount = ccount = len(line)
    print(wcount)
    print(lcount)
    print(ccount)
    print(f.read()) 
else: 
    print('file not present')
