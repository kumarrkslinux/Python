
```python 
from nsetools import Nse
import json
nse = Nse()
top_gainers = nse.get_top_gainers()
new = top_gainers[0:-1]
for com in new:
    val = f" company name: {com['symbol']} Todays Current Price: {com['ltp']}"
    print(val)
