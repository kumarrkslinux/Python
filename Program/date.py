#!/usr/bin/python3.6
import os

os.system("date")
os.system("dmidecode -t1 |grep Manufacturer |awk '{print $1 $2}'")
