```python
with open('server', 'r') as kumar:
    for i in kumar:
        print(i.strip())
```

```python
file = open('server', 'r')
read = file.readlines()
print(read)
```
```python
lines = [ 'HAI', "How are you"]
with open('server', 'a') as kumar:
      KO=kumar.write('\n'.join(lines))
      print(KO)
```
    
