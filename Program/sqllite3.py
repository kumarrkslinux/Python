#!/usr/bin/python3
import sqlite3

connection = sqlite3.connect("/home/kumar/python/Program/DB1.db")

cursor = connection.cursor()

cursor.execute("SELECT * from student")

ans = cursor.fetchall()

for i in ans:
    print(i)
