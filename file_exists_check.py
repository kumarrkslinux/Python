#!/usr/bin/python3
import os
if os.path.isfile('/tmp/newfile'):
   print ( "File exist" )
else:
   print ( "File not present" )
