#!/usr/bin/python3.6

course  = {'Tamil', 'English', 'Maths', 'science', 'social', 'English'}

course1 = {'Tamil', 'English', 'matrix', 'comerce', 'arts'}

print(course)

print ('Maths' in course)

print(course.intersection(course1))

print(course.difference(course1))

print(course.union(course1))
