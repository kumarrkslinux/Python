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
for persentage in studentdetail:
    if count%3 == 0:
<<<<<<< HEAD
      if int(new_persentage) > 75: 
         print(persentage)
    count=count+1 
=======
       if int(persentage) > 75:
          print(persentage)
    count = count+1
>>>>>>> e5db7c4ffd8be2e8d2d795d95ae5ba8f0bd0c395
