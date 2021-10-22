#!/usr/bin/python3

import os 

fname = input("Enter file name with location: ") 

if os.path.isfile(fname): 
    print("File is Present") 
    f=open(fname,'r') 
    print(f.read()) 
else: 
    print('file not present')
