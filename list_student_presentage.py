#!/usr/bin/python3
studentdetail = []
print(len(studentdetail))

student_count = int(input("Hello," "please enter the number of student in the class: "))

for student in range(student_count):
    Name, age, persentage = input("please enter the name, age, persentage sperated by space: ").split()
    print( Name, age, persentage )
    studentdetail.append(Name)
    studentdetail.append(age)
    studentdetail.append(persentage)
    print(studentdetail)

count = 1
print( "student Name", "student age", "student persentage", end=' ')
print()
print("--------------------------------------------------", end=' ')
print()
for new_persentage in studentdetail:
    if count%3 == 0:
      if int(new_persentage) > 75: 
         print(studentdetail[count -3])
         print(studentdetail[count -2])
    count=count=1 
