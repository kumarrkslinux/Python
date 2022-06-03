```python

import requests
import json

URL = 'https://github.com/kumarrkslinux/Python/new/master/Program'
response = requests.post(URL)
response2 = response.json()
Key = response2['access_token']

input_value = input("Enter the app site detail ")
appname = requests.get(input_value, headers={ "Accept" : "application/json", "Authorization": f"Bearer {Key}"})
data = appname.json()
print(data)
