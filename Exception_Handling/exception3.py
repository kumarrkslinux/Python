#!/usr/bin/python3.6
import sys

inputlist = ['a', 0, 2, 8, 10, False]

for entry in inputlist:
    try: 
        print("The Entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("OOPS!", sys.exc_info()[1], "Occured.")
        print("Next Entry")
        print()
print(" The reciprocal of", entry, "is", r)
