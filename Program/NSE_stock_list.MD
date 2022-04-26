```python
from nsetools import Nse
nse = Nse()
stockname = "Stock.txt"
with open(stockname, "r") as allstock:
     for i in allstock:
         N = nse.get_quote(i.rstrip())['lastPrice']
         print(i, N)
