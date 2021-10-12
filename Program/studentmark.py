#!/usr/bin/python3

student_count = int(input('Enter the number of Students: '))

report = {}

subjects = ('tamil', 'English', 'Maths', 'Science', 'socialscience')

for student in range(student_count):
    name = input('Enter the name of the student %d: ' % (student +1))
    
    marks = []
    for subject in subjects:
        marks.append(int(input('Enter the name of the student %s: ' % subject )))

    report[name] = marks 

for name, marks in report.items():
    total = sum(marks)

    print("%s's total marks %d" % (name, total))

    if total < 120: 

        print ("%s failed :(" % name )

    else:

        print ("%s passed :)" % name )
