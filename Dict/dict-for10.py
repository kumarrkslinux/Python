#!/usr/bin/python3
# total salary
emp_salary =  {'sakthi': 7000 , 'arun': 3000 , 'sathu': 6000, 'madu': 2000, 'kathir': 2000, 'kathir': 22000 }

total_income = 0

for key in sorted(emp_salary):
    print(key, ':', emp_salary[key])
    total_income += emp_salary[key]

for value in emp_salary.values():
    total_income += value

print(total_income)
