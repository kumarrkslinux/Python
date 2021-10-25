#!/usr/bin/python3.6

import csv

with open("student.csv", 'w' ) as f:
    w = csv.writer(f)
    w.writerow(['Name', 'number', 'Persentage', 'Department'])

    while True: 

     name = input("Enter your name: " )
     Roll_number =int(input("Enter your Roll number: "))
     Persentage = int(input("Enter your Persentage: "))
     Department = input("Enter your Department; ")
     w.writerow(['Name', 'number', 'Persentage', 'Department'])
     option = input("continue? Yes|No: ")
     if option.lower() == 'no':
         break
