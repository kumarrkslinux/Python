#!/usr/bin/python3
import sqlite3

connection = sqlite3.connect("/home/kumar/python/Program/DB1.db")

cursor = connection.cursor()

student_data = [("Thiru","C","M","75.2","1998-05-17"), ("Raja","B","F","75.2","1998-04-17"), ("Bala","A","M","72.2","1999-05-17")]

for p in student_data: 
      format_str = """INSERT INTO Student(No, Sname, Grade, Gender, Average,DATE_BIRTH) VALUES(Null,"{name}","{gr}","{gender}","{avg}", "{DATE_BIRTH}");"""
      # { } space holder
      sql_command = format_str.format(name=p[0],gr=p[1],gender=p[2], avg=p[3],DATE_BIRTH=p[4])
      cursor.execute(sql_command)
connection.commit()
connection.close()
print("Record added")

