#!/usr/bin/python3

#emp_detail = { 'name': 'sakthi', 'age': 44, 'location': 'chennai', 'hight': 160, 'weight': 64 }

emp_detail =  {'sakthi': 'name1', 44: 'age', 'chennai': 'location', 'sakthi': 'name',  160: 'hight', 64: 'weight'}

new_emp_detail = {}
for key,value in emp_detail.items():
#    print(key,':', value)
#    new_emp_detail[value] = 786
    new_emp_detail[value] = key # duplicate key & value will remove
print(new_emp_detail)
