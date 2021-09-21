#!/usr/bin/python3
studentdetail = ['Kumar', '24', '76', 'kanan', '34', '73']
count = 1
for persentage in studentdetail:
    if count%3 == 0:
       if int(persentage) > 75:
          print(persentage)
    count = count+1
