```python
#!/usr/bin/python3.6
import spwd

user_list = spwd.getspall()

for u in user_list:
     if 'ldap_user' in u:
        print('The users is present database', u.sp_namp)
