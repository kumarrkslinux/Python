#!/usr/bin/python3.6
import os

UPTIME=os.popen("uptime | awk '{ print $3 $4}' |cut -d, -f1")

UPREAD=UPTIME.read()

print("server update is", UPREAD)
