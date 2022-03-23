```python
#!/usr/bin/python3.6
import spwd

user_list = spwd.getspall()

for u in user_list:
     if 'krajak111' in u:
        print('The users is present database', u.sp_namp)
