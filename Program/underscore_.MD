```python
>>> 5 + 4
9
>>> _     # stores the result of the above expression
9
>>> _ + 6
15
>>> _
15
>>> a = _  # assigning the value of _ to another variable
>>> a
15

a, _, b = (1, 2, 3) # a = 1, b = 3
print(a, b)

for _ in range(5):
    print(_)

languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)
