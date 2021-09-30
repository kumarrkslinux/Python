#!/usr/bin/python3

#emp_detail = { 'name': 'sakthi', 'age': 44, 'location': 'chennai', 'hight': 160, 'weight': 64 }
emp_salary =  {'sakthi': 7000 , 'arun': 3000 , 'sathu': 6000, 'Madu': 2000, 'kathir': 2000 }

moresalary_emp = {}
for key,value in emp_salary.items():
    if value >= 5000:
        moresalary_emp[key] = value
        #print(key, ':', value)
print(moresalary_emp)
