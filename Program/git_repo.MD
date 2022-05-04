```python
import requests
import json
api_url = "https://api.github.com/users/kumarrkslinux/repos"
pesponse1 = requests.get(api_url)
presponse2 = pesponse1.json()
for i in presponse2:
    print(i['html_url'])
