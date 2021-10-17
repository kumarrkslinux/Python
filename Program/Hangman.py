#!/usr/bin/python3
name = input("what is your name: ")

print(name.upper() + " welcome" )

guess = ''

sentence = "python"

attems = 10 

while attems > 0: 
    failure = 0 
    for word in sentence:
        if word in guess:
            print(word, end=' ')
        else: 
            print("_", end=' ')
            failure = failure + 1
    if failure == 0:
       print("\n success!!")
       break
    print()
    guesses = input("Type one words: ")
    guess = guess + guesses

    if guess not in sentence: 
       attems = attems -1 
       print("Wrong")
       print("you can try", + attems, "times" )
       if attems == 0:
          print("you can try again" )
