#!/usr/bin/python3.6
course  = ['Tamil', 'English', 'Maths', 'science', 'social']

course_1 = ['arts', 'electronics']

number = [1,4,5,3,2] 

#1.

#sorted(course)

#sorted_value = sorted(course)

#print(sorted_value)

#2

#course.extend(course_1)
#print(course)

#3
#course.append(course_1)
#print(course)

#4
#course.insert(0,course_1)
#print(course)

#5

#course.append(course_1)
#print(course)

#course.remove('Tamil')
#print(course)

#course.pop()
#popup = course.pop()
#print(popup)
#print(course)

#course.reverse()
#print(course)

#course.sort()
#print(course)
#number.sort(reverse=True)
#print(number)


print(sum(number))
print(min(number))
print(max(number))

print(course.index('Maths'))

print('Art' in course)

for index, value in enumerate(course, start=1):
    print(index,value)
    
course_str = ' - '.join(course)

course_list = course_str.split('-')

print(course_str)
print(course_list)

