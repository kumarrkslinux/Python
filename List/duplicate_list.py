#!/usr/bin/python3
vegitables = [ 'potato', 'tomoto', 'onion', 'beans', 'onion' ]
vegitables.reverse()
if vegitables.count('onion') > 1:
   vegitables.remove('onion')
print(vegitables)
