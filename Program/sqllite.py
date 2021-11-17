
import sqlite3

connection = sqlite3.connect("C:\\Users\krajak111\DB1.db")

cursor = connection.cursor()

sql_command = """create table student(NO INTEGER PRIMARY KEY,SNAME VARCHAR(10),GRADE CHAR(1),GENDER CHAR(1),AVERAGE DECIMAL(5,2),DATE_BIRTH DATE);"""

cursor.execute(sql_command)

sql_command ="""insert into student(NO,SNAME,GRADE,AVERAGE,GRADE,DATE_BIRTH)values(10,"kannan",'A','M', "87.5",2010-12-20);"""

cursor.execute(sql_command)

connection.commit()
print("Student Table Created")
