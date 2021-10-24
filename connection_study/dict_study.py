#!/usr/bin/python3.6

student = {'name': 'Anilkumar', 'age': 37, 'courses':['English', 'Tamil'], 1: 'anubu'}

print(student)

print(student['name'])
print(student['courses'])
print(student[1])

print(student.get('age'))
print(student.get('City'))
print(student.get('City', 'Not found'))

student['phone'] = '995566-8899'
student['name'] = 'Anil'

print(student)

student.update({'name': 'Anilkumar', 'age': 39, 'phone': '995566-8899'})

print(student)

del student['phone']
print(student)

new_age = student.pop('age')
print(student)

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
