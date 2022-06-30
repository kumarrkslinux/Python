
```python 

import hvac

def vaultread():
    client = hvac.Client(url ="https://vault.hvac.com/",token ="s.xxxxxxxxxxxxxxxxxx")                               
    newdata = client.read('secret/new_account_password')
    return newdata

print(vaultread())

--------------------------------------------------------------------------------------------
import hvac

def vaultread(token):
    client = hvac.Client(url ="https://vault.hvac.com/",token=token)
    newdata = client.read('secret/new_account_password')
    return newdata
    
print(vaultread(tokenpassword))
