#!/usr/bin/python3

emp_salary =  {'sakthi': 7000 , 'arun': 3000 , 'sathu': 6000, 'madu': 2000, 'kathir': 2000, 'kathir': 22000 }

for value in sorted(emp_salary.items(),key=lambda item: item[1]):
    print(value)
