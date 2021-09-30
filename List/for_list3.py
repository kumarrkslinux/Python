#!/usr/bin/python3

# Need to change the value of numbers second value 
latter = [ 'anbu', 'anil', 'sudhan', 'vel']

number = [ 50, 400, 150, 200]

both = [ latter, number ]

for i in range(len(both)):
  for j in range(len(both[i])):
      if i == 1 and j == 1:
           both [i] [j] = 150

print(both)
