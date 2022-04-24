
```python 
from nsetools import Nse
nse = Nse()
top_gainers = nse.get_top_gainers()
new = top_gainers[0:-1]
for com in new:
    val = f" company name: {com['symbol']} Todays Current Price: {com['ltp']}"
    print('TOP GAINER TODAY', val)

print("===========================================================")

from nsetools import Nse
nse = Nse()
top_looser = nse.get_top_losers()
new = top_looser[0:-1]
for com in new:
    val = f" company name: {com['symbol']} Todays Current Price: {com['ltp']}"
    print('TOP LOOSER TODAY', val)
