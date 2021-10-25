#!/usr/bin/python3.6

import csv

with open("student.csv", 'w' ) as f:
    w = csv.writer(f)
    w.writerow(['Name', 'Number', 'Persentage', 'Department'])

    while True: 

     name = input("Enter your name: " )
     Roll_number =int(input("Enter your Roll number: "))
     Persen = int(input("Enter your Persentage: "))
     Departm = input("Enter your Department; ")
     w.writerow(['name', 'Roll_number', 'Persen', 'Departm'])
     option = input("continue? Yes|No: ")
     if option.lower() == 'no':
         break
