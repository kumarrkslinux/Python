- List is a collection which is ordered and changeable. Allows duplicate members. -- Mutable - [] 
- Tuple is a collection which is ordered and unchangeable and sequencial data. Allows duplicate members. -- Immutable - () 
- Set is a collection which is unordered and unindexed. No duplicate members. {} -- Immutable 
- Dictionary is a collection which is ordered* and changeable. No duplicate members. -- { key:value } or { items } - Key --> Uniqe, value --> can change / ​key - string ,int , tuple

# empty list
```python
empty_list = []
empty_list = list()
```
# empty tubles 

```python
empty_tuble = ()
empty_tuble = tuble()
```

# empty set
```python
empty_set = {} # it is not correct . Its dict
empty_set = set()
```

### List:-

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```
### Tuples:-

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.  Tuples are written with round brackets.

 ```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

### Set:- 

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items. 

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

### Dictionary:-

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

 ```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
``` 
