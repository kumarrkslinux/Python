#!/usr/bin/python3
word=input("Enter the word: ")
length=len(word)
countofalphbets=0
countofnumbers=0
countofspecial=0

if length < 8 :
    print("!!!!!!!!!we required minimum 8 charater!!!!!!!!!!!!")
else: 
    for number in range(length):
        if ( word[number].isalpha() ):
               countofalphbets += 1
        elif( word[number].isdigit() ):
                countofnumbers += 1
        else: 
                countofspecial = countofspecial +1

print (countofalphbets, "alphabets are present")
print (countofnumbers, "numbers are present")
print (countofspecial, "sepcialcharaters are present")
print()
