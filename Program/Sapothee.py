#!/usr/bin/python3

from random import randint

choices = [ "saa", "boo", "three" ]

compute_choices = choices[randint(0,2)]

player = False

while player == False:
      player = input(" saa, boo, three? " )
      if compute_choices == player:
         print ("Tie")
      elif player == "saa":
         if compute_choices == "boo":
            print ("You lose", compute_choices, "compute won", player )
         else:
            print ("You win", player, "lose", compute_choices )
      elif player == "poo":
         if compute_choices == "three":  
            print ("You lose", compute_choices, "compute won", player )
         else:
            print ("You win", player, "lose", compute_choices )
      elif player == "three":
         if compute_choices == "saa":  
            print ("You lose", compute_choices, "compute won", player )         
         else:
            print ("You win", player, "lose", compute_choices )
      else:
         print("please check your spelling")
      player = False 
      compute_choices = choices[randint(0,2)]
