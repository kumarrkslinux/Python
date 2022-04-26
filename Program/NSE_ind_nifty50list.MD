```python
import pandas as pd
url = "https://www1.nseindia.com/content/indices/ind_nifty50list.csv"
read_1 = pd.read_csv(url, usecols=['Company Name','Symbol'])
print(read_1)
