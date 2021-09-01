#!/usr/bin/python3.6
import os
hostname = "centos7.kms.com"

response = os.system("ping -c 1 " + hostname )

if response == 0:
   print (hostname, 'is up')
else:
  print (hostname, 'is down')
