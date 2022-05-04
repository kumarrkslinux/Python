### Python read log files and get lines containing specific words

```python 
file_name = "/var/log/messages"

with open(file_name, 'r' ) as readservername:
     for i in readservername: 
        if "kernel" in i:
             print(i)
