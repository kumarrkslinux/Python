
```python
import os
import commands

service_name = input("Enter your server: ")

def check_service_status(service_name):
    status = os.system('systemctl status ' +service_name+'>/dev/null')
    return status

def main():

   if (check_service_status(service_name) == 0):
      print service_name, "is Running"

   else:
      print service_name, "is not running"

main()
