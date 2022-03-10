```
with open('server', 'r') as kumar:
    for i in kumar:
        print(i.strip())
```

```
file = open('server', 'r')
read = file.readlines()
print(read)
```
```
lines = [ 'HAI', "How are you"]
with open('server', 'a') as kumar:
    # for i in kumar:
      KO=kumar.write('\n'.join(lines))
      print(KO)
```
    
